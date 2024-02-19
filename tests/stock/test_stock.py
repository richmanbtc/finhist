from unittest import TestCase
from src.finhist.stock import read_sp500
from ..testing.utils import check_data


class TestStock(TestCase):
    def test_read_sp500(self):
        df = read_sp500()
        check_data(self, df)
        self.assertEqual(df.loc[(1871, 1), 'sp500'], 4.44)
