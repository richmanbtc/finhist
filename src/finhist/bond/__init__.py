import os
import pandas as pd

def read_gs10():
    return _read_dgs('GS10')

def read_dgs2():
    return _read_dgs('DGS2')

def read_dgs10():
    return _read_dgs('DGS10')

def read_dgs30():
    return _read_dgs('DGS30')

def read_dgs3mo():
    return _read_dgs('DGS3MO')

def read_tbill3m_yield_census():
    # https://www2.census.gov/library/publications/2004/compendia/statab/123ed/hist/hs-39.pdf
    dir = os.path.dirname(__file__)
    df = pd.read_csv(os.path.join(dir, 'tbill3m_yield_census.csv'))
    df = df.set_index('year')
    return df

def _read_dgs(name):
    # https://fred.stlouisfed.org/series/{name}
    dir = os.path.dirname(__file__)
    df = pd.read_csv(os.path.join(dir, f'{name}.csv'))
    df.columns = [x.lower() for x in df.columns]
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df = df.drop(columns='date')
    df = df.loc[df[name.lower()] != '.']
    df[name.lower()] = df[name.lower()].astype('float')
    df = df.groupby(['year', 'month']).mean()
    df = df.sort_index()
    return df

def _read_gs(name):
    # https://fred.stlouisfed.org/series/{name}
    dir = os.path.dirname(__file__)
    df = pd.read_csv(os.path.join(dir, f'{name}.csv'))
    df.columns = [x.lower() for x in df.columns]
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df = df.drop(columns='date')
    df = df.set_index(['year', 'month'])
    return df
