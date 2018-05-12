
import unittest
from strings.time_conversion import timeConversion


class TestStrings(unittest.TestCase):


    def test_time_conversion(self):
        self.assertEqual(timeConversion("11:03:05AM"), "11:03:05")
        self.assertEqual(timeConversion("11:03:05PM"), "23:03:05")
        self.assertEqual(timeConversion("12:59:05PM"), "12:59:05")
        self.assertEqual(timeConversion("12:59:05AM"), "00:59:05")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()