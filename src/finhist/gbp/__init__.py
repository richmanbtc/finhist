import os
import pandas as pd

def read_mbm0ukm():
    # https://fred.stlouisfed.org/series/MBM0UKM
    dir = os.path.dirname(__file__)
    df = pd.read_csv(os.path.join(dir, 'MBM0UKM.csv'))
    df.columns = [x.lower() for x in df.columns]
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['mbm0ukm'] *= 1e6
    df = df.drop(columns='date')
    df = df.set_index(['year', 'month'])
    return df
