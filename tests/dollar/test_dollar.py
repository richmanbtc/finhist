from unittest import TestCase
import numpy as np
from src.finhist.dollar import read_m2sl, read_bogmbase, read_m2_census


class TestDollar(TestCase):
    def test_read_m2sl(self):
        df = read_m2sl()
        self.assertFalse(np.any(df.index.duplicated()))
        self.assertEqual(df.loc[(1959, 1), 'm2sl'], 286.6e9)

    def test_read_bogmbase(self):
        df = read_bogmbase()
        self.assertFalse(np.any(df.index.duplicated()))
        self.assertEqual(df.loc[(1959, 1), 'bogmbase'], 50500e6)

    def test_read_m2_census(self):
        df = read_m2_census()
        self.assertFalse(np.any(df.index.duplicated()))
        self.assertEqual(df.loc[1867, 'm2'], 1.28e9)

