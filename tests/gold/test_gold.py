from unittest import TestCase
from src.finhist.gold import read_gold_nma, read_gold_prod_world
from ..testing.utils import check_data


class TestGold(TestCase):
    def test_read_gold_nma(self):
        df = read_gold_nma()
        check_data(self, df)
        self.assertEqual(df.loc[1833, 'gold'], 18.93)

    def test_read_gold_prod_world(self):
        df = read_gold_prod_world()
        check_data(self, df)
        self.assertEqual(df.loc[1681, 'gold_prod'], 6)

