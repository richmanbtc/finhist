import numpy as np
import pandas as pd

def calc_implied_bond(bond_yield, duration, samples_per_year):
    return (1 - duration * bond_yield.diff().fillna(0) / 100
            + bond_yield / 100 / samples_per_year).cumprod()

def smart_concat(dfs, log=False):
    # output index: sorted(set sum(dfs index))
    # each column: auto scale and concat. overlaps are averaged
    # scaling of first data frame == 1

    if log:
        dfs = [df.apply(np.log) for df in dfs]

    sers = []
    for col in dfs[0].columns:
        ser = smart_concat_series([df[col] for df in dfs])
        sers.append(ser)

    df = pd.concat(sers, axis=1)
    df = df.sort_index()

    if log:
        df = df.apply(np.exp)

    return df


def smart_concat_series(sers):
    sers = [ser.dropna().astype('float') for ser in sers]

    ser_output = pd.concat(sers)
    ser_output = ser_output.loc[~ser_output.index.duplicated()]
    ser_output = ser_output.sort_index()
    ser_output[:] = 0.0
    ser_sum = ser_output.copy()
    ser_sum[:] = 0.0

    for ser in sers:
        ser_sum[ser.index] += ser

    n = ser_output.shape[0]
    m = len(sers)
    mask = np.zeros((n, m))
    for i in range(m):
        mask[:, i] = ser_output.index.isin(sers[i].index) * 1.0
    count = np.sum(mask, axis=1)
    avg = ser_sum.values / count

    # linear regression
    bs = []
    mats = []
    for i in range(m):
        # shifted sers[i] == output ser
        ser_temp = ser_output.copy()
        ser_temp[sers[i].index] = sers[i].values
        b = ser_temp.values - avg
        mat = mask / count.reshape(-1, 1)
        mat[:, i] -= 1

        bs.append(b[mask[:, i] > 0])
        mats.append(mat[mask[:, i] > 0])

    b = np.concatenate(bs)
    mat = np.vstack(mats)

    x = np.linalg.pinv(mat) @ b
    x -= x[0]

    ser_output[:] = avg + (mask @ x) / count
    return ser_output
