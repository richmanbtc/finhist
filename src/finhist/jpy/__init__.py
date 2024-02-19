import os
import pandas as pd

def read_jpy_m2():
    # https://www.stat-search.boj.or.jp/ssi/cgi-bin/famecgi2?cgi=$nme_a000&lstSelection=MD02
    dir = os.path.dirname(__file__)
    dfs = [
        pd.read_csv(os.path.join(dir, 'nme_R031.5998.20240219194232.01.csv'), skiprows=1),
        pd.read_csv(os.path.join(dir, 'nme_R031.6330.20240219194406.01.csv'), skiprows=1),
        pd.read_csv(os.path.join(dir, 'nme_R031.7259.20240219194913.01.csv'), skiprows=1),
    ]
    dfs[0] = dfs[0].rename(columns={ 'Ｍ２／平／マネーストック': 'jpy_m2' })
    dfs[1] = dfs[1].rename(columns={ '（更新停止）Ｍ２＋ＣＤ／平／マネーサプライ（2008年4月まで）': 'jpy_m2' })
    dfs[2] = dfs[2].rename(columns={ '（更新停止）旧Ｍ２＋ＣＤ／平／マネーサプライ（1999年3月まで）': 'jpy_m2' })

    dfs2 = []
    for df in dfs:
        df['year'] = df['系列名称'].str[:4].astype('int')
        df['month'] = df['系列名称'].str[5:].astype('int')
        dfs2.append(df)

    df = pd.concat(dfs2)
    df = df[['year', 'month', 'jpy_m2']]
    df = df.set_index(['year', 'month']).sort_index()
    df = df.dropna()
    df = df.loc[~df.index.duplicated(keep='last')]
    return df


def read_jpy_yield():
    # https://www.stat-search.boj.or.jp/ssi/cgi-bin/famecgi2?cgi=$nme_a000&lstSelection=IR01
    dir = os.path.dirname(__file__)
    df = pd.read_csv(os.path.join(dir, 'nme_R031.13609.20240219201551.01.csv'), skiprows=1)

    df = df.rename(columns={ '基準割引率および基準貸付利率': 'jpy_yield' })
    df['year'] = df['系列名称'].str[:4].astype('int')
    df['month'] = df['系列名称'].str[5:].astype('int')

    df = df[['year', 'month', 'jpy_yield']]
    df = df.set_index(['year', 'month']).sort_index()
    df = df.dropna()
    return df

def read_jpy_cpi():
    # https://www.stat-search.boj.or.jp/ssi/cgi-bin/famecgi2?cgi=$nme_a000&lstSelection=PR01
    # 2020年基準
    dir = os.path.dirname(__file__)
    df = pd.read_csv(os.path.join(dir, 'nme_R031.2504.20240219202601.02.csv'), skiprows=1)

    df = df.rename(columns={ '[国内企業物価指数] 総平均': 'jpy_cpi' })
    df['year'] = df['系列名称'].str[:4].astype('int')
    df['month'] = df['系列名称'].str[5:].astype('int')

    df = df[['year', 'month', 'jpy_cpi']]
    df = df.set_index(['year', 'month']).sort_index()
    df = df.dropna()
    return df

def read_usdjpy():
    # https://www.stat-search.boj.or.jp/ssi/cgi-bin/famecgi2?cgi=$nme_a000&lstSelection=FM08
    dir = os.path.dirname(__file__)
    df = pd.read_csv(os.path.join(dir, 'nme_R031.19695.20240219222133.02.csv'), skiprows=1)

    df = df.rename(columns={ '東京市場　ドル・円　スポット　17時時点/月中平均': 'usdjpy' })
    df['year'] = df['系列名称'].str[:4].astype('int')
    df['month'] = df['系列名称'].str[5:].astype('int')

    rows = []
    for i in range(12 * 1945 + 8 - 1, 12 * 1947 + 3 - 1):
        rows.append({ 'year': i // 12, 'month': i % 12 + 1, 'usdjpy': 15 })
    for i in range(12 * 1947 + 3 - 1, 12 * 1948 + 7 - 1):
        rows.append({ 'year': i // 12, 'month': i % 12 + 1, 'usdjpy': 50 })
    for i in range(12 * 1948 + 7 - 1, 12 * 1949 + 4 - 1):
        rows.append({ 'year': i // 12, 'month': i % 12 + 1, 'usdjpy': 270 })
    for i in range(12 * 1949 + 4 - 1, 12 * 1971 + 12 - 1):
        rows.append({ 'year': i // 12, 'month': i % 12 + 1, 'usdjpy': 360 })
    for i in range(12 * 1971 + 12 - 1, 12 * 1972 + 1 - 1):
        rows.append({ 'year': i // 12, 'month': i % 12 + 1, 'usdjpy': 308 })
    df = pd.concat([
        pd.DataFrame(rows),
        df,
    ])

    df = df[['year', 'month', 'usdjpy']]
    df = df.set_index(['year', 'month']).sort_index()
    df = df.dropna()
    return df
