import os
import pandas as pd
import re

def read_eur_m2():
    # https://data.ecb.europa.eu/data/datasets/BSI/BSI.M.U2.N.V.M20.X.1.U2.2300.Z01.E
    dir = os.path.dirname(__file__)
    df = pd.read_csv(os.path.join(dir, 'ECB Data Portal_20240219191335.csv'))
    df = df.rename(columns={ 'Monetary aggregate M2 reported by MFIs, central gov. and post office giro institutions in the euro area (stocks) (BSI.M.U2.N.V.M20.X.1.U2.2300.Z01.E)': 'eur_m2' })
    df['DATE'] = pd.to_datetime(df['DATE'])
    df['year'] = df['DATE'].dt.year
    df['month'] = df['DATE'].dt.month
    df = df.set_index(['year', 'month']).sort_index()
    df = df[['eur_m2']]
    df['eur_m2'] *= 1e6
    return df

def read_eurusd():
    # https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/eurofxref-graph-usd.en.html
    dir = os.path.dirname(__file__)

    with open(os.path.join(dir, 'usd.xml')) as f:
        s = f.read()

    rows = []
    for m in re.finditer(r'TIME_PERIOD="(.+?)" OBS_VALUE="(.+?)"', s):
        rows.append({
            'date': m.group(1),
            'eurusd': float(m.group(2))
        })
    df = pd.DataFrame(rows)
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df = df.groupby(['year', 'month']).mean()
    df = df.sort_index()
    return df
