
import unittest
from bits.exclusive_or import xoring


class TestExclusiveOr(unittest.TestCase):


    def test_xoring(self):
        self.assertEqual(xoring([1, 2, 3]), 0)
        self.assertEqual(xoring([1, 1, 3]), 3)
        self.assertEqual(xoring([1, 1, 3, 2, 3]), 2)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()