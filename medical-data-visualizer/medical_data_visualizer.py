import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
height_in_m_sq = round(((df["height"]) / 100) ** 2, 2)
BMI = round(df["weight"] / height_in_m_sq, 2)

df['overweight'] = (BMI > 25).astype(int)

# 3
df["cholesterol"] = df["cholesterol"].apply(lambda x: 0 if x == 1 else 1)
df["gluc"] = df["gluc"].apply(lambda x: 0 if x == 1 else 1)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(
        df, 
        id_vars=['cardio'], 
        value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])


    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    

    # 7
    sns.catplot(data=df_cat, kind='bar', x='variable', y='total', hue='value', col='cardio')
    draw_cat_plot()
    plt.show()


    # 8
    fig = sns.catplot(data=df_cat, kind='bar', x='variable', y='total', hue='value', col='cardio')


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[(df["ap_lo"] <= df["ap_hi"]) & (df["height"] >= df["height"].quantile(0.025))
                 & (df["height"] <= df["height"].quantile(0.975)) & (df["weight"] >= df["weight"].quantile(0.025))
                 & (df["weight"] <= df["weight"].quantile(0.975))]

    # 12
    corr = df.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))



    # 14
    fig, ax = plt.subplots(figsize=(11, 9))

    # 15
    sns.heatmap(corr, mask=mask, cmap='RdYlGn', vmin=-1, vmax=1, center=0, annot=True, square=True, linewidths=.5, cbar_kws={"shrink": .5})



    # 16
    fig.savefig('heatmap.png')
    return fig
