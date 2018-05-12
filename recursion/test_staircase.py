
import unittest
from recursion.staircase import count, non_recursive_count


class TestStaircase(unittest.TestCase):


    def test_count(self):
        self.assertEqual(count(0), 1)
        self.assertEqual(count(1), 1)
        self.assertEqual(count(2), 2)
        self.assertEqual(count(3), 4)
        self.assertEqual(count(4), 7)
        self.assertEqual(count(5), 13)
        self.assertEqual(count(6), 24)
        self.assertEqual(count(7), 44)
        self.assertEqual(count(8), 81)

    def test_non_recursive_count(self):
        self.assertEqual(non_recursive_count(0), 1)
        self.assertEqual(non_recursive_count(1), 1)
        self.assertEqual(non_recursive_count(2), 2)
        self.assertEqual(non_recursive_count(3), 4)
        self.assertEqual(non_recursive_count(4), 7)
        self.assertEqual(non_recursive_count(5), 13)
        self.assertEqual(non_recursive_count(6), 24)
        self.assertEqual(non_recursive_count(7), 44)
        self.assertEqual(non_recursive_count(8), 81)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()