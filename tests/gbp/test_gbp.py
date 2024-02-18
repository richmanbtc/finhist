from unittest import TestCase
import numpy as np
from src.finhist.gbp import read_mbm0ukm


class TestGbp(TestCase):
    def test_read_mbm0ukm(self):
        df = read_mbm0ukm()
        self.assertFalse(np.any(df.index.duplicated()))
        self.assertEqual(df.loc[(1870, 1), 'mbm0ukm'], 123.86e6)


