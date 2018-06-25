import unittest
from example import lettersCombinations



class TestCircleArea(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(lettersCombinations(""), [])
        self.assertAlmostEqual(lettersCombinations("23"), ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])


