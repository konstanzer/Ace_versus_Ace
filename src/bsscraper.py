import sqlite3
import pandas as pd
import urllib.request


def savant_call(season, team, place, csv=False, sep=';'):
    """
    Breaks data into team, year, and place for small file sizes.
    Args: int, str, str, bool, str
    Returns: csv or dataframe
    """
    # Generate the URL
    url = ("https://baseballsavant.mlb.com/statcast_search/csv?all=true&"
           "hfPT=&hfAB=&hfGT=R%7C&hfPR=&hfZ=&stadium=&hfBBL=&hfNewZones=&"
           f"hfPull=&hfC=&hfSea={season}%7C&hfSit=&player_type=pitcher&hfOuts=&"
           "opponent=&pitcher_throws=&batter_stands=&hfSA=&game_date_gt=&"
           f"game_date_lt=&hfInfield=&team={team}&position=&hfOutfield=&hfRO=&"
           f"home_road={place}&hfFlag=&hfBBT=&metric_1=&hfInn=&min_pitches=0&"
           "min_results=0&group_by=name&sort_col=pitches&player_event_sort="
           "api_p_release_speed&sort_order=desc&min_pas=0&type=details&")
    
    file_name = f'{team}_{season}_{place}.csv'
    # Returns csv if csv is True
    return urllib.request.urlretrieve(url, file_name) if csv else pd.read_csv(url)


teams = ['LAA', 'HOU', 'OAK', 'TOR', 'ATL', 'MIL', 'STL','CHC', 'ARI', 
         'LAD', 'SF', 'CLE', 'SEA', 'MIA', 'NYM', 'WSH', 'BAL', 'SD', 
         'PHI', 'PIT', 'TEX', 'TB', 'BOS', 'CIN', 'COL', 'KC', 'DET', 
         'MIN', 'CWS', 'NYY']


def make_database(db_name, seasons, teams=teams):
    """
    Creates a database with all teams unless othrwise specified.
    Args: str, list, list
    Returns: None
    """
    savant = sqlite3.connect(f'{db_name}.db')
    
    where = ['Home', 'Road']
    # Loop over seasons and teams appending to statcast table at each iteration.
    for season in seasons:
        for team in teams:
            for place in where:
                pd.io.sql.to_sql(savant_call(season, team, place),
                                 name='statcast', con=savant, if_exists='append')

    savant.commit()
    savant.close()

    
if __name__ == "__main__":
    savant_call(2020, 'NYY', 'Away', True)
