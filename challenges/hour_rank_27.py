
import unittest
import math
import sys

def is_sorted(arr):
    if not arr:
        return False

    _sorted = True
    i = 0
    while _sorted and i < len(arr) - 1:
        i += 1
        _sorted = _sorted and arr[i] >= arr[i - 1]

    return _sorted, i

def make_avg(arr, index):
    if index == 0 or index == len(arr) - 1:
        return arr
    v1 = arr[index - 1]
    v2 = arr[index + 1]
    v = int(math.ceil(float(v1 + v2) / 2))
    arr[index] = v
    return arr

def find_larger(arr, start, a):
    for i in xrange(start, len(arr)):
        if arr[i] > a:
            return arr[i], i
    return None, None

def max_prof(p):
    _max = -sys.maxint
    for i in xrange(0, len(p)):
        first = p[i]
        if i == len(p) - 1:
            continue
        second, index = find_larger(p, i, first)
        if second is None:
            continue
        else:
            if index == len(p) - 1:
                continue
            third, _ = find_larger(p, index, second)
            if third is None:
                continue
            else:
                r = first * second * third
                if r > _max:
                    _max = r
    return _max

class TestChallenge(unittest.TestCase):

    def test_is_sorted(self):
        case1 = [5, 7, 7, 11, 15, 12, 22, 24]
        result, first_unsorted = is_sorted(case1)
        self.assertFalse(result)
        self.assertEqual(case1[first_unsorted], 12)

    def test_make_avg(self):
        case1 = [5, 7, 7, 11, 15, 12, 22, 24]
        _, first_unsorted = is_sorted(case1)
        case_avg = make_avg(case1, first_unsorted)
        self.assertListEqual(case_avg, [5, 7, 7, 11, 15, 19, 22, 24])

    def test_find_max(self):
        p = [10, 2, -10, 6, 1, 0, 8]
        _max = max_prof(p)
        self.assertEqual(_max, 96)
        
    def test_find_max_3(self):
        expected = 1881594571297920
        with open('input03.txt') as f:
            line = f.readline()
            numbers = line.split()
            numbers = [int(n) for n in numbers]
        _max = max_prof(numbers)
        self.assertEqual(expected, _max)
    
    def test_find_max_9(self):
        expected = 999957000501998440
        with open('input09.txt') as f:
            line = f.readline()
            numbers = line.split()
            numbers = [int(n) for n in numbers]
        _max = max_prof(numbers)
        self.assertEqual(expected, _max)

    def test_find_max_12(self):
        expected = -1000
        with open('input12.txt') as f:
            line = f.readline()
            numbers = line.split()
            numbers = [-int(n) for n in numbers]
        _max = max_prof(numbers)
        self.assertEqual(expected, _max)
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
