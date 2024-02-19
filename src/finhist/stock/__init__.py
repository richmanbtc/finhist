import os
import pandas as pd


def read_sp500():
    # https://datahub.io/core/s-and-p-500
    dir = os.path.dirname(__file__)
    df = pd.read_csv(os.path.join(dir, 'sp500.csv'))
    df.columns = [x.lower() for x in df.columns]
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df = df.drop(columns='date')
    df = df.set_index(['year', 'month'])
    return df

def read_nikkei225():
    # https://www.macrotrends.net/2593/nikkei-225-index-historical-chart-data
    dir = os.path.dirname(__file__)
    df = pd.read_csv(os.path.join(dir, 'nikkei-225-index-historical-chart-data.csv'), skiprows=15)
    df.columns = [x.lower() for x in df.columns]
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df = df.drop(columns='date')
    df = df.groupby(['year', 'month']).mean()
    df = df.rename(columns={ ' value': 'nikkei225' })
    return df
