from unittest import TestCase
from src.finhist.gbp import read_mbm0ukm
from ..testing.utils import check_data


class TestGbp(TestCase):
    def test_read_mbm0ukm(self):
        df = read_mbm0ukm()
        check_data(self, df)
        self.assertEqual(df.loc[(1870, 1), 'mbm0ukm'], 123.86e6)


