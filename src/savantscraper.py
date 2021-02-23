
# -*- coding: utf-8 -*-
"""Load detail level Baseball Savant data into an SQLite database."""

import os
from time import sleep
from urllib.error import HTTPError
import sqlite3
import pandas as pd
from tqdm.auto import tqdm


def savant_search(season, team, home_road, csv=False, sep=';'):
    """Return detail-level Baseball Savant search results.

    Breaks pieces by team, year, and home/road for reasonable file sizes.

    Args:
        season (int): the year of results.
        team (str): the modern three letter team abbreviation.
        home_road (str): whether the pitching team is "Home" or "Road".
        csv (bool): whether or not a csv
        sep (str): separat

    Returns:
        a pandas dataframe of results and optionally a csv.

    Raises:
        HTTPError: if connection is unsuccessful multiple times.

    """
    # Define the number of times to retry on a connection error
    num_tries = 6
    # Define the starting backoff time to grow exponentially
    pause_time = 30

    # Generate the URL to search based on team and year
    url = ("https://baseballsavant.mlb.com/statcast_search/csv?all=true"
           "&hfPT=&hfAB=&hfBBT=&hfPR=&hfZ=&stadium=&hfBBL=&hfNewZones=&hfGT=&h"
           f"fC=&hfSea={season}%7C&hfSit=&player_type=pitcher&hfOuts=&opponent"
           "=&pitcher_throws=&batter_stands=&hfSA=&game_date_gt=&game_date_lt="
           f"&hfInfield=&team={team}&position=&hfOutfield=&hfRO="
           f"&home_road={home_road}&hfFlag=&hfPull=&metric_1=&hfInn="
           "&min_pitches=0&min_results=0&group_by=name&sort_col=pitches"
           "&player_event_sort=pitch_number_thisgame&sort_order=desc"
           "&min_pas=0&type=details&")

    # Attempt to download the file
    # If unsuccessful retry with exponential backoff
    # If still unsuccessful raise HTTPError
    # Due to possible limit on access to this data
    for retry in range(0, num_tries):
        try:
            single_combination = pd.read_csv(url, low_memory=False)
        except HTTPError as connect_error:

            if connect_error:
                if retry == num_tries - 1:
                    raise HTTPError
                else:
                    sleep(pause_time)
                    pause_time *= 2
                    continue
            else:
                break

    # Drop duplicate and deprecated fields
    single_combination.drop(['pitcher.1', 'fielder_2.1', 'umpire', 'spin_dir',
                             'spin_rate_deprecated', 'break_angle_deprecated',
                             'break_length_deprecated', 'tfs_deprecated',
                             'tfs_zulu_deprecated'], axis=1, inplace=True)

    # Optionally save as csv for loading to another file system
    if csv:
        single_combination.to_csv(f"{team}_{season}_{home_road}_detail.csv",
                                  index=False, sep=sep)

    return single_combination if not csv else None


def database_import(db_name, seasons, teams=None, reload=True):
    """Load detail-level Baseball Savant search results into SQLite database.

    Creates a database if it does not exist and loads all teams by default.
    All data is loaded into a single table named statcast.

    Args:
        db_name (str): name given to the SQLite database file.
        seasons (tuple): inclusive range of years to include.
        teams (list): list of specific teams to include. Default is all.
        reload (bool): delete database with the same name.

    Returns:
        an SQLite database loaded with defined data.

    Raises:
        HTTPError: if connection is unsuccessful multiple times.

    """
    # Delete the database if it exists based on argument
    if reload:
        try:
            os.remove(f"{db_name}.db")
        except OSError:
            pass

    # Connect to the database
    savant = sqlite3.connect(f"{db_name}.db")

    # Define teams to be iterated over
    if teams is None:
        teams = ['LAA', 'HOU', 'OAK', 'TOR', 'ATL', 'MIL', 'STL',
                 'CHC', 'ARI', 'LAD', 'SF', 'CLE', 'SEA', 'MIA',
                 'NYM', 'WSH', 'BAL', 'SD', 'PHI', 'PIT', 'TEX',
                 'TB', 'BOS', 'CIN', 'COL', 'KC', 'DET', 'MIN',
                 'CWS', 'NYY']

    locations = ['Home', 'Road']

    # Loop over seasons and teams
    # Append to statcast table at each iteration
    for season in tqdm(range(seasons[0], seasons[1]+1), desc='Seasons'):
        for team in tqdm(teams, desc='Teams'):
            for location in tqdm(locations, desc='Home/Road', leave=False):
                single_combination = savant_search(season, team, location)
                pd.io.sql.to_sql(single_combination, name='statcast',
                                 con=savant, if_exists='append')

    # Close connection
    savant.commit()
    savant.close()


if __name__ == '__main__':

    # Example for two years and two teams
    database_import('baseball_savant', (2017, 2018), teams=['STL', 'COL'])
