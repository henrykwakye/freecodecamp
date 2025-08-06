import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Original Data')


    # Create first line of best fit
    res1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred1 = pd.Series(range(1880, 2051))
    y_pred1 = res1.slope * x_pred1 + res1.intercept
    plt.plot(x_pred1, y_pred1, 'r', label='Fit: All Data')


    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000]
    res2 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    x_pred2 = pd.Series(range(2000, 2051))
    y_pred2 = res2.slope * x_pred2 + res2.intercept
    plt.plot(x_pred2, y_pred2, 'g', label='Fit: 2000+ Data')


    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.legend()

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()