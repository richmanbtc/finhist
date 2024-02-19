from unittest import TestCase
from src.finhist.cny import (
    read_cny_m2, read_usdcny
)
from ..testing.utils import check_data


class TestJpy(TestCase):
    def test_read_cny_m2(self):
        df = read_cny_m2()
        check_data(self, df)
        self.assertEqual(df.loc[(1998, 12), 'cny_m2'], 10449850000000)

    def test_read_usdcny(self):
        df = read_usdcny()
        check_data(self, df)
        self.assertEqual(df.loc[(1981, 1), 'usdcny'], 1.5523809523809524)
