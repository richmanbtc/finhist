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

def read_m0_census():
    # page 992-993 https://www2.census.gov/library/publications/1975/compendia/hist_stats_colonial-1970/hist_stats_colonial-1970p2-chX.pdf
    dir = os.path.dirname(__file__)
    df = pd.read_csv(os.path.join(dir, 'm2_census.csv'))
    df['m0'] *= 1e9
    df = df.set_index('year')
    return df

def read_cpi_frb():
    # https://www.minneapolisfed.org/about-us/monetary-policy/inflation-calculator/consumer-price-index-1913-
    dir = os.path.dirname(__file__)
    df = pd.read_csv(os.path.join(dir, 'cpi_frb.csv'))
    df = df.set_index('year')
    return df

def read_cpi_frb_1800():
    # https://www.minneapolisfed.org/about-us/monetary-policy/inflation-calculator/consumer-price-index-1800-
    dir = os.path.dirname(__file__)
    df = pd.read_csv(os.path.join(dir, 'cpi_frb_1800.csv'))
    df = df.set_index('year')
    return df

def read_total_salary():
    # https://fred.stlouisfed.org/series/BA06RC1A027NBEA
    dir = os.path.dirname(__file__)
    df = pd.read_csv(os.path.join(dir, 'BA06RC1A027NBEA.csv'))
    df = df.rename(columns={ 'BA06RC1A027NBEA': 'total_salary' })
    df.columns = [x.lower() for x in df.columns]
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    df['total_salary'] *= 1e9
    df = df.drop(columns='date')
    df = df.set_index(['year'])
    return df
