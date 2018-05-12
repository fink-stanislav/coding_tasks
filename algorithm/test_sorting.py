
import unittest

from algorithm.sorting import bubble_sort, merge_sort, quick_sort


class TestSorting(unittest.TestCase):

    def test_bubble(self):
        arr = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
        result = bubble_sort(arr)
        self.assertListEqual(result, [1, 3, 4, 6, 9, 14, 20, 21, 21, 25])

    def test_merge(self):
        arr = [21, 4, 1, 3, 9, 20, 25]
        result = merge_sort(arr)
        self.assertListEqual(result, [1, 3, 4, 9, 20, 21, 25])
    
    def test_quicksort(self):
        arr = [21, 4, 1, 3, 9, 20, 25]
        result = quick_sort(arr, 0, len(arr) - 1)
        self.assertListEqual(result, [1, 3, 4, 9, 20, 21, 25])

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()