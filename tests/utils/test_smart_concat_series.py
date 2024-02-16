from unittest import TestCase
import pandas as pd
from pandas.testing import assert_series_equal
from src.finhist.utils import smart_concat_series
import numpy as np


class TestSmartConcatSeries(TestCase):
    def test_ok(self):
        input = [
            pd.Series([100, 150], index=[1, 2]),
            pd.Series([0, 50], index=[2, 3]),
        ]
        expected = pd.Series([100, 150, 200], index=[1, 2, 3]).astype('float')

        output = smart_concat_series(input)
        assert_series_equal(output, expected)

    def test_ok2(self):
        input = [
            pd.Series([0, 100, 200], index=[1, 2, 3]),
            pd.Series([0, 0, 100], index=[2, 3, 4]),
        ]
        expected = pd.Series([0, 125, 175, 250], index=[1, 2, 3, 4]).astype('float')

        output = smart_concat_series(input)
        assert_series_equal(output, expected)

    def test_ok3(self):
        input = [
            pd.Series([0, 100], index=[1, 2]),
            pd.Series([50, 100], index=[2, 3]),
            pd.Series([20, 30], index=[3, 4]),
        ]
        expected = pd.Series([0, 100, 150, 160], index=[1, 2, 3, 4]).astype('float')

        output = smart_concat_series(input)
        assert_series_equal(output, expected)

    def test_ok4(self):
        input = [
            pd.Series([150, 100], index=[2, 1]),
            pd.Series([0, 50, np.nan], index=[2, 3, 1]),
        ]
        expected = pd.Series([100, 150, 200], index=[1, 2, 3]).astype('float')

        output = smart_concat_series(input)
        assert_series_equal(output, expected)
