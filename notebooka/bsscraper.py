import sqlite3
import pandas as pd
import urllib


def savant_call(season, team, csv=False, sep=';'):
    """
    Breaks data into team and year for reasonable file sizes.
    """
    # Generate the URL to search based on team and year.
    url = ("https://baseballsavant.mlb.com/statcast_search/csv?all=true"
           "&hfPT=&hfAB=&hfBBT=&hfPR=&hfZ=&stadium=&hfBBL=&hfNewZones=&hfGT=&h"
           f"fC=&hfSea={season}%7C&hfSit=&player_type=pitcher&hfOuts=&opponent"
           "=&pitcher_throws=&batter_stands=&hfSA=&game_date_gt=&game_date_lt="
           f"&hfInfield=&team={team}&position=&hfOutfield=&hfRO="
           "&home_road=&hfFlag=&hfPull=&metric_1=&hfInn="
           "&min_pitches=0&min_results=0&group_by=name&sort_col=pitches"
           "&player_event_sort=pitch_number_thisgame&sort_order=desc"
           "&min_pas=0&type=details&")
    
    # Returns csv if csv is True or a Dataframe otherwise.
    return urllib.request.urlretrieve(url, f'{team}_{season}.csv') if csv else pd.read_csv(url)


def make_database(db_name, seasons, teams):
    """
    Creates a database. All data is loaded into a single table named statcast.
    """
    # Create and connect to the database.
    savant = sqlite3.connect(f'{db_name}.db')

    # Loop over seasons and teams appending to statcast table at each iteration.
    for season in seasons:
        for team in teams:
            pd.io.sql.to_sql(savant_call(season, team), name='statcast', con=savant, if_exists='append')

    # Close connection
    savant.commit()
    savant.close()

    
if __name__ == "__main__":
    #Example csv output of 2020 Yankees pitching data.
    savant_call(2020, "NYY", csv=True)