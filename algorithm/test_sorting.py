
import unittest

import algorithm.sorting as alg_sort


class TestSorting(unittest.TestCase):

    def test_bubble(self):
        arr = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
        result = alg_sort.bubble_sort(arr)
        self.assertListEqual(result, [1, 3, 4, 6, 9, 14, 20, 21, 21, 25])

    def test_mergesort1(self):
        arr = [21, 4, 1, 3, 9, 20, 25]
        result = alg_sort.merge_sort(arr)
        self.assertListEqual(result, [1, 3, 4, 9, 20, 21, 25])
    
    def test_quicksort(self):
        arr = [21, 4, 1, 3, 9, 20, 25]
        result = alg_sort.quick_sort(arr, 0, len(arr) - 1)
        self.assertListEqual(result, [1, 3, 4, 9, 20, 21, 25])

    def test_mergesort2(self):
        a = [9,8,4,6,4,8,9,4,6,4,5,4,1]
        a = alg_sort.merge_sort(a)
        self.assertListEqual(a, [1, 4, 4, 4, 4, 4, 5, 6, 6, 8, 8, 9, 9])

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()