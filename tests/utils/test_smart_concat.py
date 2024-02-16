from unittest import TestCase
import pandas as pd
from pandas.testing import assert_frame_equal
from src.finhist.utils import smart_concat


class TestSmartConcat(TestCase):
    def test_ok(self):
        input = [
            pd.DataFrame([
                [100, 10], [150, 20]
            ], index=[1, 2], columns=['a', 'b']),
            pd.DataFrame([
                [0, 10], [50, 30]
            ], index=[2, 3], columns=['a', 'b']),
        ]
        expected = pd.DataFrame(
            [[100, 10], [150, 20], [200, 40]],
            index=[1, 2, 3],
            columns=['a', 'b'],
        ).astype('float')

        output = smart_concat(input)
        assert_frame_equal(output, expected)

    def test_log(self):
        input = [
            pd.DataFrame([[100], [150]], index=[1, 2], columns=['a']),
            pd.DataFrame([[10], [20]], index=[2, 3], columns=['a']),
        ]
        expected = pd.DataFrame(
            [[100], [150], [300]],
            index=[1, 2, 3],
            columns=['a'],
        ).astype('float')

        output = smart_concat(input, log=True)
        assert_frame_equal(output, expected)
