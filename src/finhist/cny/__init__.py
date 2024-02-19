import os
import pandas as pd
import re

def read_cny_m2():
    # https://fred.stlouisfed.org/series/MYAGM2CNM189N
    dir = os.path.dirname(__file__)
    df = pd.read_csv(os.path.join(dir, 'MYAGM2CNM189N.csv'))
    df = df.rename(columns={ 'MYAGM2CNM189N': 'cny_m2' })
    df.columns = [x.lower() for x in df.columns]
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df = df.drop(columns='date')
    df = df.set_index(['year', 'month'])
    return df

def read_usdcny():
    # https://www.macrotrends.net/2575/us-dollar-yuan-exchange-rate-historical-chart
    dir = os.path.dirname(__file__)
    df = pd.read_csv(os.path.join(dir, 'us-dollar-yuan-exchange-rate-historical-chart.csv'), skiprows=15)
    df.columns = [x.lower() for x in df.columns]
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df = df.drop(columns='date')
    df = df.groupby(['year', 'month']).mean()
    df = df.rename(columns={ ' value': 'usdcny' })
    return df
