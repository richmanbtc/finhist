from unittest import TestCase
import numpy as np
from src.finhist.stock import read_sp500


class TestStock(TestCase):
    def test_read_sp500(self):
        df = read_sp500()
        self.assertFalse(np.any(df.index.duplicated()))
        self.assertEqual(df.loc[(1871, 1), 'sp500'], 4.44)
