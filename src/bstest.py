import scipy.stats as scs
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


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


def print_test_results(df, df1, df1_mean, player1, df2, df2_mean, player2, pitch, stat):
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
    avg_cats = ['release_speed', 'release_spin_rate','pfx_x',
                'pfx_z','vx0','vy0','vz0','ax','ay','az']

    agg = pd.concat([c.agg('sum')[ps].sum(axis=1),
                    d.agg('sum')[ps].sum(axis=1)], axis=1).rename(columns={0: "Cole", 1: "deGrom"})

    cole_mean = c.agg('mean')[avg_cats]
    degrom_mean = d.agg('mean')[avg_cats]
    
    
    #Tests
    #Pitch speeds
    print_test_results(df, cole, cole_mean, 'Cole',
                       degrom, degrom_mean, 'deGrom',
                       'FF', 'release_speed')
    
    print_test_results(df, cole, cole_mean, 'Cole',
                       degrom, degrom_mean, 'deGrom',
                       'SL', 'release_speed')
    
    print_test_results(df, cole, cole_mean, 'Cole',
                       degrom, degrom_mean, 'deGrom',
                       'CU', 'release_speed')
    
    print_test_results(df, cole, cole_mean, 'Cole',
                       degrom, degrom_mean, 'deGrom',
                       'CH', 'release_speed')
    
    #Pitch spins
    print_test_results(df, cole, cole_mean, 'Cole',
                       degrom, degrom_mean, 'deGrom',
                       'FF', 'release_spin_rate')
    
    print_test_results(df, cole, cole_mean, 'Cole',
                       degrom, degrom_mean, 'deGrom',
                       'SL', 'release_spin_rate')
    
    print_test_results(df, cole, cole_mean, 'Cole',
                       degrom, degrom_mean, 'deGrom',
                       'CU', 'release_spin_rate')
    
    print_test_results(df, cole, cole_mean, 'Cole',
                       degrom, degrom_mean, 'deGrom',
                       'CH', 'release_spin_rate')
    
    #Lateral movment
    print_test_results(df, cole, cole_mean, 'Cole',
                       degrom, degrom_mean, 'deGrom',
                       'FF', 'pfx_x')
    
    print_test_results(df, cole, cole_mean, 'Cole',
                       degrom, degrom_mean, 'deGrom',
                       'SL', 'pfx_x')
    
    print_test_results(df, cole, cole_mean, 'Cole',
                       degrom, degrom_mean, 'deGrom',
                       'CU', 'pfx_x')
    
    print_test_results(df, cole, cole_mean, 'Cole',
                       degrom, degrom_mean, 'deGrom',
                       'CH', 'pfx_x')
    
    #Vertical movement
    print_test_results(df, cole, cole_mean, 'Cole',
                       degrom, degrom_mean, 'deGrom',
                       'FF', 'pfx_z')
    
    print_test_results(df, cole, cole_mean, 'Cole',
                       degrom, degrom_mean, 'deGrom',
                       'SL', 'pfx_z')
    
    print_test_results(df, cole, cole_mean, 'Cole',
                       degrom, degrom_mean, 'deGrom',
                       'CU', 'pfx_z')
    
    print_test_results(df, cole, cole_mean, 'Cole',
                       degrom, degrom_mean, 'deGrom',
                       'CH', 'pfx_z')