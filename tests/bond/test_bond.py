from unittest import TestCase
import numpy as np
from src.finhist.bond import read_dgs10, read_dgs2, read_dgs30, read_gs10, read_tbill3m_yield_census


class TestBond(TestCase):
    def test_read_gs10(self):
        df = read_gs10()
        self.assertFalse(np.any(df.index.duplicated()))
        self.assertEqual(df.loc[(1953, 4), 'gs10'], 2.83)

    def test_read_dgs10(self):
        df = read_dgs10()
        self.assertFalse(np.any(df.index.duplicated()))
        self.assertEqual(df.loc[(1962, 1), 'dgs10'], 4.083181818181818)

    def test_read_dgs2(self):
        df = read_dgs2()
        self.assertFalse(np.any(df.index.duplicated()))
        self.assertEqual(df.loc[(1976, 6), 'dgs2'], 7.06)

    def test_read_dgs30(self):
        df = read_dgs30()
        self.assertFalse(np.any(df.index.duplicated()))
        self.assertEqual(df.loc[(1977, 2), 'dgs30'], 7.754444444444443)

    def test_read_tbill3m_yield_census(self):
        df = read_tbill3m_yield_census()
        self.assertFalse(np.any(df.index.duplicated()))
        self.assertEqual(df.loc[1920, 'tbill3m_yield'], 5.42)
