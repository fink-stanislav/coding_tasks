
import unittest
import bits.counting as bc


class TestCounting(unittest.TestCase):


    def test_sum_bit_diffs(self):
        arr = [1, 3, 5]
        self.assertEqual(bc.sum_bit_diffs(arr), 8)

    def test_power(self):
        x = 50
        y = 5
        p = 13
        r1 = bc.power(x, y, p)
        r2 = x ** y % p
        self.assertEqual(r1, r2)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_sum_bit_diffs']
    unittest.main()