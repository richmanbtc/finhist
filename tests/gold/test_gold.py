from unittest import TestCase
import numpy as np
from src.finhist.gold import read_gold_nma


class TestGold(TestCase):
    def test_read_gold_nma(self):
        df = read_gold_nma()
        self.assertFalse(np.any(df.index.duplicated()))
        self.assertEqual(df.loc[1833, 'gold'], 18.93)
