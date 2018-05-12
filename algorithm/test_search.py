
import unittest

from algorithm.search import binary_search


class TestSearch(unittest.TestCase):


    def test_binary_search(self):
        test_list = [1,3,9,11,15,19,29]
        test_val1 = 25
        test_val2 = 15
        self.assertEqual(binary_search(test_list, test_val1), -1)
        self.assertEqual(binary_search(test_list, test_val2), 4)

        self.assertEqual(binary_search(test_list, 1), 0)
        self.assertEqual(binary_search(test_list, 3), 1)
        self.assertEqual(binary_search(test_list, 9), 2)
        self.assertEqual(binary_search(test_list, 11), 3)
        self.assertEqual(binary_search(test_list, 15), 4)
        self.assertEqual(binary_search(test_list, 19), 5)
        self.assertEqual(binary_search(test_list, 29), 6)

        self.assertEqual(binary_search(test_list, 2), -1)
        self.assertEqual(binary_search(test_list, 4), -1)
        self.assertEqual(binary_search(test_list, 10), -1)
        self.assertEqual(binary_search(test_list, 12), -1)
        self.assertEqual(binary_search(test_list, 16), -1)
        self.assertEqual(binary_search(test_list, 20), -1)
        self.assertEqual(binary_search(test_list, 30), -1)

        self.assertEqual(binary_search(test_list, 0), -1)
        self.assertEqual(binary_search(test_list, 2), -1)
        self.assertEqual(binary_search(test_list, 8), -1)
        self.assertEqual(binary_search(test_list, 10), -1)
        self.assertEqual(binary_search(test_list, 14), -1)
        self.assertEqual(binary_search(test_list, 18), -1)
        self.assertEqual(binary_search(test_list, 28), -1)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()