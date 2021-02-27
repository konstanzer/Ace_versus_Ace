import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def dual_stacked_barchart(df1, df2, labels, pitches, legend):
    '''
    Stacked barchart of pitch frequencies
    '''
    g1 = df1.groupby('pitch_type')
    g2 = df2.groupby('pitch_type')
    pitch_totals = pd.concat([g1.agg('sum')[pitches].sum(axis=1),
                            g2.agg('sum')[pitches].sum(axis=1)],
                            axis=1).rename(columns={0: labels[0], 1: labels[1]})

    fig, ax = plt.subplots(figsize=(12,3))
    #Make font readable or slides
    plt.rc('font', **{'weight':'bold', 'size':16})

    fig, ax = plt.subplots(figsize=(12,3))
    pitch_totals.T.plot(kind='barh', stacked=True, ax=ax)
    ax.legend(legend, bbox_to_anchor=(1, 1))
    ax.set_title('Frequency of various pitch types')
    ax.set_xlabel('total pitches thrown')
    plt.tight_layout()

    #Save
    plt.savefig('visuals/stacked_bar_pitches.png')


def dual_box_plot(stat, df1, df2, labels):
    '''
    Args: list, str, str, str
    '''
    fig, ax = plt.subplots(figsize=(5,8))
    #Make font readable or slides
    plt.rc('font', **{'weight':'bold', 'size':16})

    ax.set_ylabel(stat)
    ax.boxplot([df1[stat], df2[stat]], labels=labels)
    plt.tight_layout()

    #Save
    plt.savefig(f'visuals/{stat}_boxplot.png')


def density_plot(stat, df, name, legend, clip=None):
    '''
    Args: str, str, series, series, list, str
    '''
    fig, ax = plt.subplots(figsize=(12,3))

    sns.set_theme(style='ticks')
    sns.color_palette('hls', 8)

    ax.set_title(name)
    ax.set_xlabel(stat)

    #Make font readable or slides
    plt.rc('font', **{'weight':'bold', 'size':16})

    #Plots density curves by pitch.
    sns.kdeplot(df[stat], hue=df['pitch_type'], fill=True, alpha=.5,
            linewidth=2, clip=clip)
    
    #Make sure legend labels are in order
    ax.legend(legend, bbox_to_anchor=(1, 1))
    plt.tight_layout()

    #Save
    plt.savefig(f'visuals/{name}_{stat}_density.png')


if __name__ == "__main__":
    
    #Load data
    df = pd.read_csv('aces_2020.csv')
    cole = df[df.pitcher==543037]
    degrom = df[df.pitcher==594798]

    labels = ['Cole', 'deGrom']

    dual_stacked_barchart(cole, degrom, labels, ['CH','CU','FF','SL'],
                            legend=['Changeup','Curveball','Fastball','Slider'])

    #Boxplots
    dual_box_plot('release_speed', cole, degrom, labels)
    dual_box_plot('pfx_x', cole, degrom, labels)
    dual_box_plot('pfx_z', cole, degrom, labels)
    dual_box_plot('release_spin_rate', cole, degrom, labels)
    
    #Density plots
    legend0 = ['Curveball', 'Changeup', 'Slider', 'Fastball']
    legend1 = ['Curveball', 'Changeup', 'Fastball', 'Slider']

    density_plot('release_speed', cole, labels[0], legend0)
    density_plot('release_speed', degrom, labels[1], legend1)

    density_plot('release_spin_rate', cole, labels[0], legend0)
    density_plot('release_spin_rate', degrom, labels[1], legend1)

    density_plot('pfx_x', cole, labels[0], legend0)
    density_plot('pfx_x', degrom, labels[1], legend1)

    density_plot('pfx_z', cole, labels[0], legend0)
    density_plot('pfx_z', degrom, labels[1], legend1)