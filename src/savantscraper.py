import os
from time import sleep
import sqlite3
import pandas as pd


def savant_search(season, team, csv=False, sep=';'):
    """
    Breaks pieces by team, year for reasonable file sizes.

    Args:
        season (int): the year of results.
        team (str): the modern three letter team abbreviation.
        csv (bool): whether or not a csv
        sep (str): separat

    Returns:
        a pandas dataframe of results and optionally a csv.
    """

    # Generate the URL to search based on team and year
    url = ("https://baseballsavant.mlb.com/statcast_search/csv?all=true"
           "&hfPT=&hfAB=&hfBBT=&hfPR=&hfZ=&stadium=&hfBBL=&hfNewZones=&hfGT=&h"
           f"fC=&hfSea={season}%7C&hfSit=&player_type=pitcher&hfOuts=&opponent"
           "=&pitcher_throws=&batter_stands=&hfSA=&game_date_gt=&game_date_lt="
           f"&hfInfield=&team={team}&position=&hfOutfield=&hfRO="
           f"&home_road=&hfFlag=&hfPull=&metric_1=&hfInn="
           "&min_pitches=0&min_results=0&group_by=name&sort_col=pitches"
           "&player_event_sort=pitch_number_thisgame&sort_order=desc"
           "&min_pas=0&type=details&")
    
    single_combination = pd.read_csv(url, low_memory=False)

    # Drop duplicate and deprecated fields
    single_combination.drop(['pitcher.1', 'fielder_2.1', 'umpire', 'spin_dir',
                             'spin_rate_deprecated', 'break_angle_deprecated',
                             'break_length_deprecated', 'tfs_deprecated',
                             'tfs_zulu_deprecated'], axis=1, inplace=True)

    # Optionally save as csv for loading to another file system
    if csv:
        single_combination.to_csv(f"{team}_{season}_detail.csv",
                                  index=False, sep=sep)

    return single_combination if not csv else None


def database_import(db_name, seasons, teams):
    """
    Creates a database. All data is loaded into a single table named statcast.

    Args:
        db_name (str): name given to the SQLite database file.
        seasons (tuple): inclusive range of years to include.
        teams (list): list of specific teams to include. Default is all.

    Returns:
        an SQLite database loaded with defined data.
    """
    
    # Connect to the database
    savant = sqlite3.connect(f"{db_name}.db")

    # Loop over seasons and teams
    # Append to statcast table at each iteration
    for season in seasons:
        for team in teams:
            single_combination = savant_search(season, team)
            pd.io.sql.to_sql(single_combination, name='statcast', 
                             con=savant, if_exists='append')

    # Close connection
    savant.commit()
    savant.close()
