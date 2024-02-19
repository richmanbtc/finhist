from unittest import TestCase
import numpy as np
from src.finhist.jpy import (
    read_jpy_m2, read_jpy_yield, read_jpy_cpi
)


class TestJpy(TestCase):
    def test_read_jpy_m2(self):
        df = read_jpy_m2()
        self.assertFalse(np.any(df.index.duplicated()))
        self.assertEqual(df.loc[(1967, 1), 'jpy_m2'], 282500)

    def test_read_jpy_yield(self):
        df = read_jpy_yield()
        self.assertFalse(np.any(df.index.duplicated()))
        self.assertEqual(df.loc[(1882, 10), 'jpy_yield'], 10.22)

    def test_read_jpy_cpi(self):
        df = read_jpy_cpi()
        self.assertFalse(np.any(df.index.duplicated()))
        self.assertEqual(df.loc[(1960, 1), 'jpy_cpi'], 48.2)
