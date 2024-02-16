import os
import pandas as pd

def read_m2sl():
    # https://fred.stlouisfed.org/series/M2SL
    dir = os.path.dirname(__file__)
    df = pd.read_csv(os.path.join(dir, 'M2SL.csv'))
    df.columns = [x.lower() for x in df.columns]
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['m2sl'] *= 1e9
    df = df.drop(columns='date')
    df = df.set_index(['year', 'month'])
    return df

def read_bogmbase():
    # https://fred.stlouisfed.org/series/BOGMBASE
    dir = os.path.dirname(__file__)
    df = pd.read_csv(os.path.join(dir, 'BOGMBASE.csv'))
    df.columns = [x.lower() for x in df.columns]
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['bogmbase'] *= 1e6
    df = df.drop(columns='date')
    df = df.set_index(['year', 'month'])
    return df

def read_m2_census():
    # page 992-993 https://www2.census.gov/library/publications/1975/compendia/hist_stats_colonial-1970/hist_stats_colonial-1970p2-chX.pdf
    dir = os.path.dirname(__file__)
    df = pd.read_csv(os.path.join(dir, 'm2_census.csv'))
    df['m2'] *= 1e9
    df = df.set_index('year')
    return df
