import sqlite3
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def query_database(db_name, query):
    """
    Args: str, str
    Queries a database with specified query.
    Returns a dataframe.
    """
    # Connect to the database.
    conn = sqlite3.connect(f'{db_name}.db')
    
    df= pd.read_sql_query(query, conn)
    
    # Close connection
    conn.close()
    
    return df

    
def rename_to_curveball(df, indexes):
    '''
    Args: df, list of ints
    Renames pitch_type to CU for curveball.
    Outs: None
    '''
    for ix in indexes:
        df.at[ix, 'pitch_type'] = 'CU'
    

def onehot_encode(df, field_name):
    '''
    Args: df, str
    Encoder outputs a 2d array, then reattaches the header outputs a dataframe.
    Finally, it adds the spase array to the original df.
    Outs: dataframe
    '''
    enc = OneHotEncoder(dtype=int, sparse=False)
    x = np.array(df[field_name]).reshape(-1, 1)

    arr = enc.fit_transform(x)
    arr = np.concatenate((enc.categories_, arr))
    arr = pd.DataFrame(arr[1:], columns=arr[0], dtype=int)
    
    return pd.concat([df, arr], axis=1)


def change_values(df, field_name, to_change, change_to):
    '''
    Args: dataframe, str, list, list
    Changes values from a column based on input list.
    ResultsL None
    '''
    df.loc[:, field_name].replace(to_change, change_to, inplace=True)
    
    
def backwards_k(df):
    '''
    Args: df, str, str
    Add strikeouts looking to events.
    Outs: None
    '''
    for ix, x in enumerate(df["events"]):
        if df["events"][ix] == 'strikeout':
            if df["description"][ix] == 'called_strike':
                df["events"][ix] = 'called_' + df["events"][ix]

                
def backfiller(df, col_to_fill, col_to_fill_from):
    '''
    Args: df, str, str
    Filling in None values with another column.
    Outs: None
    '''
    for ix, x in enumerate(df[col_to_fill]):
        if x == None:
            df[col_to_fill][ix] = df[col_to_fill_from][ix]

            
def make_datetime(df):
    df['game_date'] = pd.to_datetime(df['game_date'])

    
def drop_columns(df, columns):
    '''
    Args: df, list
    Outs: df
    '''
    return df.drop(columns, axis=1)
    
    
def save_df(df, file_name):
    '''
    Args: df, str
    Outs: None
    '''
    df.to_csv(f'{file_name}.csv', index=False)

    
def player_df(df, player_name):
    '''
    Args: df, str
    Outs: df
    '''
    df = df[df['player_name'] == player_name]
    #This creates a boolean dataframe of all rows and only columns with at least 1 nonzero value.
    df = df.loc[:, (df != 0).any(axis=0)]
    
    return df

def density_plot(title, xlabel, kde_x, hue, legend_labels, file_nickname, clip=None):
    '''
    Args: str, str, series, series, list, str
    '''
    fig, ax = plt.subplots(figsize=(12,3))
    sns.set_theme(style='ticks')
    sns.color_palette('hls', 8)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    sns.kdeplot(kde_x, hue=hue, fill=True, alpha=.5, linewidth=2, clip=clip)
    #Make sure legend labels are in order
    ax.legend(legend_labels, bbox_to_anchor=(1, 1))
    plt.tight_layout()
    plt.savefig(f'visuals/{file_nickname}_density.png')


def box_plot(data, ylabel, labels, file_nickname, c='blue'):
    '''
    Args: list, str, str, str
    '''
    fig, ax = plt.subplots(figsize=(5,8))
    ax.set_ylabel(ylabel)
    ax.boxplot(data, labels=labels)
    font = {'weight' : 'bold', 'size' : 16}
    plt.rc('font', **font)

    plt.tight_layout()
    plt.savefig(f'visuals/{file_nickname}_boxplot.png')


if __name__ == "__main__":
    df = query_database('NYY_NYM_2020', '''
                        SELECT player_name, pitcher, game_date, pitch_type, pitch_name, balls,
                        strikes, release_speed, release_spin_rate, events, description, zone,
                        release_pos_x, release_pos_z, pfx_x, pfx_z, plate_x, plate_z,
                        release_extension, vx0, vy0, vz0, ax, ay, az
                        FROM statcast
                        WHERE pitch_type IS NOT NULL; ''')
    
    rename_to_curveball(df, [2000])
    
    change_values(df, 'events', ['caught_stealing_2b', 'caught_stealing_3b',
                                 'pickoff_caught_stealing_2b', 'run', 'pickoff_2b',
                                 'other_out', 'strikeout_double_play', 'interf_def',
                                 'fielders_choice_out', 'fielders_choice',
                                 'grounded_into_double_play', 'force_out', 'double_play',
                                 'sac_bunt', 'sac_fly', 'hit_by_pitch'],
                  [None, None, None, None, None, None, 'strikeout', 'field_error',
                   'field_out', 'field_out', 'field_out', 'field_out', 'field_out',
                   'field_out', 'field_out', 'walk'])
    
    change_values(df, 'description', ['foul_bunt', 'swinging_strike_blocked',
                                      'missed_bunt','foul_tip', 'foul', 'blocked_ball',
                                      'pitchout'], 
                  ['swinging_strike', 'swinging_strike', 'swinging_strike', 'swinging_strike',
                   'swinging_strike','ball', 'ball'])
    
    backwards_k(df)
    backfiller(df, "events", "description")
    
    df = onehot_encode(df, "pitch_type")
    df = df.fillna(0)
    df.CU = df.KC + df.CU
    df = drop_columns(df, ['description', 'KC'])
    
    make_datetime(df)
    
    cole = player_df(df, 'Gerrit Cole')
    degrom = player_df(df, 'Jacob deGrom')
    df = pd.concat([cole, degrom])
            
    change_values(df, 'pitch_name', ['4-Seam Fastball', 'Knuckle Curve'], ['Fastball', 'Curveball'])
    change_values(df, 'pitch_type', ['KC'], ['CU'])
    
    save_df(df, 'aces_2020')
    
    #PART 2: Visuals
    
    df = pd.read_csv('aces_2020.csv')
    cole = df[df.pitcher==543037]
    degrom = df[df.pitcher==594798]
    
    #Creating agg dataframes
    c = cole.groupby('pitch_type')
    d = degrom.groupby('pitch_type')

    ps = ['CH','CU','FF','SL']
    avg_cats = ['release_speed', 'release_spin_rate','pfx_x',
                'pfx_z','vx0','vy0','vz0','ax','ay','az']

    agg = pd.concat([c.agg('sum')[ps].sum(axis=1),
                    d.agg('sum')[ps].sum(axis=1)],
                    axis=1).rename(columns={0: "Cole", 1: "deGrom"})

    cole_mean = c.agg('mean')[avg_cats]
    degr_mean = d.agg('mean')[avg_cats]
            
        
    #Stacked barchart of pitch frequencies
    fig, ax = plt.subplots(figsize=(12,3))
    agg.T.plot(kind='barh', stacked=True, ax=ax)
    ax.legend(['Changeup','Curveball','Fastball','Slider'], bbox_to_anchor=(1, 1))
    ax.set_title('Frequency of various pitch types')
    ax.set_xlabel('total pitches thrown in 2020')
    plt.tight_layout()
    plt.savefig('visuals/stacked_bar_pitches.png')
    
    
    #Boxplots

    box_plot([cole.release_speed, degrom.release_speed], 'Release speeds (all pitches)',
             ['Cole', 'deGrom'], 'speeds')
    box_plot([cole.pfx_x, degrom.pfx_x], 'Horizontal movement (all pitches)',
             ['Cole', 'deGrom'], 'xmove', 'purple')
    box_plot([cole.pfx_z, degrom.pfx_z], 'Vertical movement (all pitches)',
             ['Cole', 'deGrom'], 'zmove', 'red')
    box_plot([cole.release_speed, degrom.release_speed], 'Release speeds (all pitches)',
             ['Cole', 'deGrom'], 'speeds')

    
    #Density plots
    density_plot('Gerrit Cole: speeds by type of pitch',
                 'Speed out of hand (mph)',
                 kde_x=cole.release_speed, hue=cole.pitch_type, 
                 legend_labels=['Curveball', 'Changeup', 'Slider', 'Fastball'],
                 file_nickname='cole_speed')
    
    density_plot('Jacob deGrom: speeds by type of pitch',
                 'Speed out of hand (mph)',
                 kde_x=degrom.release_speed, hue=degrom.pitch_type, 
                 legend_labels=['Curveball', 'Changeup', 'Fastball', 'Slider'],
                 file_nickname='degrom_speed')
    
    density_plot('Gerrit Cole: spin rates by type of pitch',
                 'Spin rate out of hand (rpm)',
                 kde_x=cole.release_spin_rate, hue=cole.pitch_type, 
                 legend_labels=['Curveball', 'Changeup', 'Slider', 'Fastball'],
                 file_nickname='cole_spin')
    
    density_plot('Jacob deGrom: speeds by type of pitch',
                 'Speed out of hand (mph)',
                 kde_x=degrom.release_spin_rate, hue=degrom.pitch_type, 
                 legend_labels=['Curveball', 'Changeup', 'Fastball', 'Slider'],
                 file_nickname='degrom_spin',
                 clip=(1230, 3100))
    
    density_plot('Gerrit Cole: horizontal movement',
                 'Horizontal movement (in.) of the pitch',
                 kde_x=cole.pfx_x, hue=cole.pitch_type, 
                 legend_labels=['Curveball', 'Changeup', 'Slider', 'Fastball'],
                 file_nickname='cole_lateral')
    
    density_plot('Jacob deGrom: horizontal movement',
                 'Horizontal movement (in.) of the pitch',
                 kde_x=degrom.pfx_x, hue=degrom.pitch_type, 
                 legend_labels=['Curveball', 'Changeup', 'Fastball', 'Slider'],
                 file_nickname='degrom_lateral')