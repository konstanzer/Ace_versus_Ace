import scipy.stats as scs
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def welch_ttest(x, df1, id1, df2, id2, pitch, stat):
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

    plt.savefig(f'visuals/ttests/ttest_{id1}_{id2}_{pitch}_{stat}.png')
    print(f'A histogram plot named ttest_{id1}_{id2}_{pitch}_{stat}.png \n'
            'was saved in ~/visuals/ttests. \n')

    result = scs.ttest_ind(stat1, stat2, equal_var=False)

    return (result[0], result[1], sum(df1.pitch_type==pitch), sum(df2.pitch_type==pitch))


def print_test_results(df, id1, id2, pitch, stat, test_stats):
    '''
    Prints the results of the t-test with means.
    '''
    x = np.linspace(df[stat].min(), df[stat].max(), 50)
    player1 = df[df.pitcher==id1]
    player2 = df[df.pitcher==id2]
    player1_means = player1.groupby('pitch_type').agg('mean')[test_stats]
    player2_means = player2.groupby('pitch_type').agg('mean')[test_stats]

    result = welch_ttest(x, player1, id1, player2, id2, pitch, stat)
    
    print(f't-test result -{pitch} -{stat}:')
    print('docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html')
    print(f'ID{id1} mean: {round(player1_means[stat][pitch],5)}')
    print(f'ID{id2} mean: {round(player2_means[stat][pitch],5)}')
    print(f't-statistic: {round(result[0],5)}')
    print(f'p-value: {result[1]}')
    print(f'ID{id1} sample size: {result[2]}')
    print(f'ID{id2} sample size: {result[3]}')


def run_tests(df, id1, id2, test_pitches, test_stats):
    '''
    Prints a Welch's t-test result for specified stats, players, and pitches.
    '''
    for stat in test_stats:
        for pitch in test_pitches:
            print_test_results(df, id1, id2, pitch, stat, test_stats)


if __name__ == "__main__":

    '''To make this more useful, have a database of all statcast data then use the input
    id to query the database and put player data into a dataframe, maybe even automate tests to look for interesting results.'''

    #Load data
    df = pd.read_csv('aces_2020.csv')
    id1 = 543037  #Cole. ID can be found in URL on Baseball Savant player page.
    id2 = 594798  #deGrom

    #Print Welch's t-test results
    stats = ['release_speed', 'release_spin_rate', 'pfx_x', 'pfx_z']
    pitches = ['FF', 'SL', 'CU', 'CH']
    run_tests(df, id1, id2, pitches, stats)