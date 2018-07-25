
import unittest
import bits.exclusive_or as xor


class TestExclusiveOr(unittest.TestCase):


    def test_xoring(self):
        self.assertEqual(xor.xoring([1, 2, 3]), 0)
        self.assertEqual(xor.xoring([1, 1, 3]), 3)
        self.assertEqual(xor.xoring([1, 1, 3, 2, 3]), 2)

    def test_swap(self):
        a1 = 5
        b1 = 6
        a2, b2 = xor.swap_ints(a1, b1)
        self.assertEqual(a1, b2)
        self.assertEqual(b1, a2)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()