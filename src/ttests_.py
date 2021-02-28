import scipy.stats as scs
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sqlite3


def query_database(db_name, query, player1, player2=None):
    '''
    Args: str, str
    Returns df.
    '''
    conn = sqlite3.connect(f'{db_name}.db')

    #For year_over_year, only one player is used
    if player2 == None:
        df = pd.read_sql_query(query, conn, params=(player1,))
    else:
        df = pd.read_sql_query(query, conn, params=(player1, player2))

    conn.close()
    
    return df


def welch_ttest(x, df1, id1, df2, id2, pitch, stat, year):
    '''
    Saves a plot of the samples distributions then returns a t-test result.
    '''
    stat1 = df1[df1.pitch_type==pitch][stat]
    stat2 = df2[df2.pitch_type==pitch][stat]

    fig, ax = plt.subplots(figsize=(7,5))
    ax.hist(stat1, alpha=.6, bins=x, label=id1)
    ax.hist(stat2, alpha=.6, bins=x, label=id2)
    ax.set_xlabel(stat)
    ax.set_title(pitch)
    ax.legend()

    plt.savefig(f'ttests/ttest_{id1}_{id2}_{pitch}_{stat}_{year}.png')
    print(f'A histogram plot named ttest_{id1}_{id2}_{pitch}_{stat}_{year}.png \n'
            'was saved in ~/ttests. \n')

    result = scs.ttest_ind(stat1, stat2, equal_var=False)

    return (result[0], result[1], sum(df1.pitch_type==pitch), sum(df2.pitch_type==pitch))


def print_test_results(df, id1, id2, pitch, stat, test_stats, year):
    '''
    Prints the results of the t-test with means.
    '''
    #If variable year is not a year but a player, then it's a year-over-year test
    try:
        int(year)
        player1 = df[df.player_name==id1]
        player2 = df[df.player_name==id2]
    except:
        player1 = df[df.game_year==id1]
        player2 = df[df.game_year==id2]

    merged = pd.concat([player1, player2])
    x = np.linspace(merged[stat].min(), merged[stat].max(), 50)
    player1_means = player1.groupby('pitch_type').agg('mean')[test_stats]
    player2_means = player2.groupby('pitch_type').agg('mean')[test_stats]

    result = welch_ttest(x, player1, id1, player2, id2, pitch, stat, year)
    
    print(f'Welch\'s t-test result -{pitch} -{stat}:')
    print(f'{id1} mean: {round(player1_means[stat][pitch],2)}')
    print(f'{id2} mean: {round(player2_means[stat][pitch],2)}')
    print(f'{id1} sample size: {result[2]}')
    print(f'{id2} sample size: {result[3]}')
    print(f't-statistic: {round(result[0],2)}')
    print(f'p-value: {result[1]}')
    print("\n")
   

def run_tests(df, id1, id2, test_pitches, test_stats, year):
    '''
    Prints a Welch's t-test result for specified stats, players, and pitches.
    '''
    for stat in test_stats:
        for pitch in test_pitches:
            print_test_results(df, id1, id2, pitch, stat, test_stats, year)


def user_input_pitch_stat():

    official_pitches = ['FF', 'SL', 'CU', 'CH', 'FS',
                        'FT', 'SC', 'FO', 'KN', 'KC', 'FC', 'SI']
    #For lateral break, player handedness must be added to compare a lefty and righty
    official_stats = ['release_speed', 'release_spin_rate', 'release_extension',
                        'release_pos_x', 'release_pos_z', 'release_pos_y', 'pfx_x',
                        'pfx_z', 'plate_x', 'plate_z', 'vx0', 'vy0', 'vz0', 'ax', 'ay',
                        'az', 'effective_speed']

    pitches, stats, pitch, stat = [], [], " ", " "
    while pitch != "":
        pitch = input("Enter pitch: ").upper()
        if pitch in official_pitches: pitches.append(pitch)
    while stat != "":
        stat = input("Enter stat: ")
        if stat in official_stats: stats.append(stat)

    print(f"Tests will be run on {pitches} for {stats}.")

    return pitches, stats


def degrom_rule(name):
    return "Jacob deGrom" if name == "Jacob Degrom" else name


def player_pair_test():

    year = input("Enter year: ")
    id1 = input("Enter Player 1: ").title()
    id2 = input("Enter Player 2: ").title()
    id1 = degrom_rule(id1)
    id2 = degrom_rule(id2)
    pitches, stats = user_input_pitch_stat()

    df = query_database(f"MLB_{year}", """SELECT player_name, pitcher, pitch_type,
        release_speed, release_spin_rate, release_extension, release_pos_x, game_year,
        release_pos_z, release_pos_y, pfx_x, pfx_z, plate_x, plate_z,
        vx0, vy0, vz0, ax, ay, az, effective_speed FROM statcast
        WHERE player_name IN (?, ?)""", id1, id2)
    
    print('\n')

    run_tests(df, id1, id2, pitches, stats, year)


def year_over_year_test():

    player = input("Enter player's name: ").title()
    player = degrom_rule(player)
    y1 = input("Enter Year 1: ")
    y2 = input("Enter Year 2: ")
    pitches, stats = user_input_pitch_stat()

    df1 = query_database(f"MLB_{y1}", """SELECT player_name, pitcher, pitch_type,
        release_speed, release_spin_rate, release_extension, release_pos_x, game_year,
        release_pos_z, release_pos_y, pfx_x, pfx_z, plate_x, plate_z,
        vx0, vy0, vz0, ax, ay, az, effective_speed FROM statcast
        WHERE player_name = ?""", player)
    
    df2 = query_database(f"MLB_{y2}", """SELECT player_name, pitcher, pitch_type,
        release_speed, release_spin_rate, release_extension, release_pos_x, game_year,
        release_pos_z, release_pos_y, pfx_x, pfx_z, plate_x, plate_z,
        vx0, vy0, vz0, ax, ay, az, effective_speed FROM statcast
        WHERE player_name = ?""", player)

    df = pd.concat([df1[df1.player_name==player], df2[df2.player_name==player]])

    print('\n')

    run_tests(df, int(y1), int(y2), pitches, stats, player)


if __name__ == "__main__":

    print('You have chosen to do a Baseball Savant Welch\'s t-test.')
    print('docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html')

    test_type = input("1 for 1 player year-over-year test.\n"
        "2 for 2 players, same year test: \n")
    
    if int(test_type)==1:
        year_over_year_test()

    if int(test_type)==2:
        player_pair_test()