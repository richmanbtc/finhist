from unittest import TestCase
from src.finhist.jpy import (
    read_jpy_m2, read_jpy_yield, read_jpy_cpi, read_usdjpy
)
from ..testing.utils import check_data


class TestJpy(TestCase):
    def test_read_jpy_m2(self):
        df = read_jpy_m2()
        check_data(self, df)
        self.assertEqual(df.loc[(1967, 1), 'jpy_m2'], 282500)

    def test_read_jpy_yield(self):
        df = read_jpy_yield()
        check_data(self, df)
        self.assertEqual(df.loc[(1882, 10), 'jpy_yield'], 10.22)

    def test_read_jpy_cpi(self):
        df = read_jpy_cpi()
        check_data(self, df)
        self.assertEqual(df.loc[(1960, 1), 'jpy_cpi'], 48.2)

    def test_read_usdjpy(self):
        df = read_usdjpy()
        check_data(self, df)
        self.assertEqual(df.loc[(1945, 8), 'usdjpy'], 15)
