import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import seaborn as sns
import numpy as np
from pandas.plotting import register_matplotlib_converters
from datetime import date
import calendar
register_matplotlib_converters()   
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv',parse_dates=['date'])

# Clean data
df = df[(df['value']<=np.percentile(df['value'],97.5))&
        (df['value']>=np.percentile(df['value'],2.5))]


def draw_line_plot():
    # Draw line plot
  x=df['date']
  y = df ['value']
  fig  = plt.figure(figsize=(20,6), dpi=200) 
  ax = fig.add_subplot(111)
  lines = plt.plot(x,y, color ='red')
  
  ax.xaxis.set_major_locator(mdates.MonthLocator(interval=6))
  ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
  datemin =date(2016, 2, 1)
  ax.set_xlim(datemin)
  ax.set_xlabel('Date')
  ax.set_ylabel('Page Views')
  ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')




    # Save image and return fig (don't change this part)
  fig.savefig('line_plot.png')
  return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.set_index('date')
    df_bar['month'] = df_bar.index.month
    df_bar['month'] = df_bar['month'].apply(lambda x: calendar.month_name[x])
    
    df_bar['year'] = df_bar.index.year

    # Draw bar plot
    chart = plt.figure(figsize=(8,7), dpi=100) 
    chart =sns.barplot(data = df_bar , x = 'year', y = 'value', hue='month', width= 0.7 ,palette='tab10', errorbar=None, hue_order=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August','September','October','November','December'])
    chart.set(ylabel = 'Average Page Views', xlabel = 'Years')
    plt.legend(title = 'Months', loc='upper left',)
    plt.xticks(rotation=90)
    fig= chart.figure



    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1, 2, figsize=(25, 6))
    chart= sns.boxplot(data=df_box, x='year',y='value', ax=ax[0] )
    chart.set (ylabel='Page Views', xlabel='Year',title='Year-wise Box Plot (Trend)')
    
    xorder =['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug','Sep','Oct','Nov','Dec']
    chart1=sns.boxplot(data=df_box, x='month',y='value',ax=ax[1],order=xorder)
    chart1.set (ylabel='Page Views', xlabel='Month',title='Month-wise Box Plot (Seasonality)')




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
