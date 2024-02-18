from unittest import TestCase
import numpy as np
from src.finhist.dollar import (
    read_m2sl, read_bogmbase, read_m2_census, read_cpi_frb,
    read_cpi_frb_1800, read_total_salary, read_total_salary2
)


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

    def test_read_cpi_frb(self):
        df = read_cpi_frb()
        self.assertFalse(np.any(df.index.duplicated()))
        self.assertEqual(df.loc[1913, 'cpi'], 9.9)

    def test_read_cpi_frb_1800(self):
        df = read_cpi_frb_1800()
        self.assertFalse(np.any(df.index.duplicated()))
        self.assertEqual(df.loc[1800, 'cpi'], 51)

    def test_read_total_salary(self):
        df = read_total_salary()
        self.assertFalse(np.any(df.index.duplicated()))
        self.assertEqual(df.loc[1982, 'total_salary'], 1479.187e9)

    def test_read_total_salary2(self):
        df = read_total_salary2()
        self.assertFalse(np.any(df.index.duplicated()))
        self.assertEqual(df.loc[(1959, 1), 'total_salary'], 252.3e9)
