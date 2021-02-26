import scipy.stats as scs
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.max_open_warning': 0})


def pitch_df(df, pitch):
    return df[df.pitch_type==pitch]


def stat_mean(mean_df, pitch, stat):
    '''
    Args: df on means, str, str
    '''
    return mean_df[stat][pitch]


def welch_ttest(df, df1, player1, df2, player2, pitch, stat):
    
    fig, ax = plt.subplots(figsize=(7,5))
    x=np.linspace(df[stat].min(), df[stat].max(), 50)
    
    ax.hist(pitch_df(df1, pitch)[stat], alpha=.6, bins=x, label=player1)
    ax.hist(pitch_df(df2, pitch)[stat], alpha=.6, bins=x, label=player2)
    ax.set_xlabel(stat)
    ax.set_title(pitch)
    ax.legend()
    plt.savefig(f'visuals/ttests/ttest_{player1}_{player2}_{pitch}_{stat}.png')

    return scs.ttest_ind(pitch_df(df1, pitch)[stat],
                         pitch_df(df2, pitch)[stat],
                         equal_var=False)


def print_test_results(pitch, stat, df, df1, df1_mean, player1, df2, df2_mean, player2):
    '''
    Args: df, df, df, str, df, df, str, str, str, int, int
    '''
    result = welch_ttest(df, df1, player1, df2, player2, pitch, stat)
    
    print(f'Welch t-test - {pitch} - {stat} - {player1} & {player2}:')
    print(f'{player1} mean: {stat_mean(df1_mean, pitch, stat)}')
    print(f'{player2} mean: {stat_mean(df2_mean, pitch, stat)}')
    print(f't-stat: {result[0]}')
    print(f'p-value: {result[1]}')
    print('\n')


if __name__ == "__main__":
    '''
    t-tests with plots
    '''
    #Load data
    df = pd.read_csv('aces_2020.csv')
    cole = df[df.pitcher==543037]
    degrom = df[df.pitcher==594798]
    
    #Create df of means
    c = cole.groupby('pitch_type')
    d = degrom.groupby('pitch_type')

    ps = ['CH','CU','FF','SL']
    avg_cats = ['release_speed', 'release_spin_rate', 'pfx_x',
                'pfx_z', 'release_extension', 'plate_x', 'plate_z',
                'vx0','vy0','vz0','ax','ay','az']

    agg = pd.concat([c.agg('sum')[ps].sum(axis=1),
                    d.agg('sum')[ps].sum(axis=1)], axis=1).rename(columns={0: "Cole", 1: "deGrom"})

    cole_mean = c.agg('mean')[avg_cats]
    degrom_mean = d.agg('mean')[avg_cats]
    
    
    #Tests
    test_stats = ['release_speed', 'release_spin_rate',
    				'pfx_x', 'pfx_z', 'release_extension']
    pitches = ['FF', 'SL', 'CU', 'CH']
    c_set = (cole, cole_mean, 'Cole')
    d_set = (degrom, degrom_mean, 'deGrom')
    

    for stat in test_stats:
    	for pitch in pitches:
    		print_test_results(pitch, stat, df,
    			c_set[0], c_set[1], c_set[2],
    			d_set[0], d_set[1], d_set[2])


