import sqlite3
import pandas as pd
import urllib


def savant_call(season, team, place, csv=False, sep=';'):
    """
    Breaks data into team and year for reasonable file sizes.
    """
    # Generate the URL to search based on team and year.
    url = ("https://baseballsavant.mlb.com/statcast_search/csv?all=true&"
           "hfPT=&hfAB=&hfGT=R%7C&hfPR=&hfZ=&stadium=&hfBBL=&hfNewZones=&"
           f"hfPull=&hfC=&hfSea={season}%7C&hfSit=&player_type=pitcher&hfOuts=&"
           "opponent=&pitcher_throws=&batter_stands=&hfSA=&game_date_gt=&"
           f"game_date_lt=&hfInfield=&team={team}&position=&hfOutfield=&hfRO=&"
           f"home_road={place}&hfFlag=&hfBBT=&metric_1=&hfInn=&min_pitches=0&"
           "min_results=0&group_by=name&sort_col=pitches&player_event_sort="
           "api_p_release_speed&sort_order=desc&min_pas=0&type=details&")
    
    # Returns csv if csv is True or a Dataframe otherwise.
    return urllib.request.urlretrieve(url, f'{team}_{season}.csv') if csv else pd.read_csv(url)


teams = ['LAA', 'HOU', 'OAK', 'TOR', 'ATL', 'MIL', 'STL','CHC', 'ARI', 
         'LAD', 'SF', 'CLE', 'SEA', 'MIA', 'NYM', 'WSH', 'BAL', 'SD', 
         'PHI', 'PIT', 'TEX', 'TB', 'BOS', 'CIN', 'COL', 'KC', 'DET', 
         'MIN', 'CWS', 'NYY']


def make_database(db_name, seasons, teams=teams):
    """
    Creates a database. Uses all teams unless othrwise specified.
    All data is loaded into a single table named statcast.
    """
    # Create and connect to the database.
    savant = sqlite3.connect(f'{db_name}.db')
    
    where = ['Home', 'Road']
    # Loop over seasons and teams appending to statcast table at each iteration.
    for season in seasons:
        for team in teams:
            for place in where:
                pd.io.sql.to_sql(savant_call(season, team, place),
                                 name='statcast', con=savant, if_exists='append')

    # Close connection
    savant.commit()
    savant.close()

    
if __name__ == "__main__":
    make_database('NYY_NYM_2020', [2020], ['NYY', 'NYM'])