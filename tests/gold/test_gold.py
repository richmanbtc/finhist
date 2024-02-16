from unittest import TestCase
import numpy as np
from src.finhist.gold import read_gold_nma, read_gold_prod_world


class TestGold(TestCase):
    def test_read_gold_nma(self):
        df = read_gold_nma()
        self.assertFalse(np.any(df.index.duplicated()))
        self.assertEqual(df.loc[1833, 'gold'], 18.93)

    def test_read_gold_prod_world(self):
        df = read_gold_prod_world()
        self.assertFalse(np.any(df.index.duplicated()))
        self.assertEqual(df.loc[1681, 'gold_prod'], 6)

