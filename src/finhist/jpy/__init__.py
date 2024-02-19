import os
import pandas as pd

def read_m2_jpy():
    # https://www.stat-search.boj.or.jp/ssi/cgi-bin/famecgi2?cgi=$nme_a000&lstSelection=MD02
    dir = os.path.dirname(__file__)
    dfs = [
        pd.read_csv(os.path.join(dir, 'nme_R031.5998.20240219194232.01.csv'), skiprows=1),
        pd.read_csv(os.path.join(dir, 'nme_R031.6330.20240219194406.01.csv'), skiprows=1),
        pd.read_csv(os.path.join(dir, 'nme_R031.7259.20240219194913.01.csv'), skiprows=1),
    ]
    dfs[0] = dfs[0].rename(columns={ 'Ｍ２／平／マネーストック': 'm2_jpy' })
    dfs[1] = dfs[1].rename(columns={ '（更新停止）Ｍ２＋ＣＤ／平／マネーサプライ（2008年4月まで）': 'm2_jpy' })
    dfs[2] = dfs[2].rename(columns={ '（更新停止）旧Ｍ２＋ＣＤ／平／マネーサプライ（1999年3月まで）': 'm2_jpy' })

    dfs2 = []
    for df in dfs:
        df['year'] = df['系列名称'].str[:4].astype('int')
        df['month'] = df['系列名称'].str[5:].astype('int')
        dfs2.append(df)

    df = pd.concat(dfs2)
    df = df[['year', 'month', 'm2_jpy']]
    df = df.set_index(['year', 'month']).sort_index()
    df = df.dropna()
    df = df.loc[~df.index.duplicated(keep='last')]
    return df
