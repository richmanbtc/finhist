from unittest import TestCase
from src.finhist.eur import (
    read_eur_m2, read_eurusd
)
from ..testing.utils import check_data


class TestJpy(TestCase):
    def test_read_eur_m2(self):
        df = read_eur_m2()
        check_data(self, df)
        self.assertEqual(df.loc[(1980, 1), 'eur_m2'], 1080273e6)

    def test_read_eurusd(self):
        df = read_eurusd()
        check_data(self, df)
        self.assertEqual(df.loc[(1999, 1), 'eurusd'], 1.1607800000000001)
