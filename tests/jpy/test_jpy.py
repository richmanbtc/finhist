from unittest import TestCase
import numpy as np
from src.finhist.jpy import (
    read_m2_jpy
)


class TestJpy(TestCase):
    def test_read_m2sl(self):
        df = read_m2_jpy()
        self.assertFalse(np.any(df.index.duplicated()))
        self.assertEqual(df.loc[(1967, 1), 'm2_jpy'], 282500)
