import numpy as np

def check_data(test_instance, df):
    test_instance.assertFalse(np.any(df.index.duplicated()))
    test_instance.assertTrue(df.index.is_monotonic_increasing)

    df = df[[]].reset_index()
    if 'month' in df.columns:
        t = 12 * df['year'] + df['month'] - 1
    else:
        t = df['year']
    test_instance.assertEqual(t.iloc[-1] - t.iloc[0] + 1, t.shape[0])
