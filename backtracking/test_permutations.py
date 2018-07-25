
import unittest
from backtracking.permutations import permute


class Test(unittest.TestCase):


    def test_permute(self):
        # Driver program to test the above function
        string = "ABCD"
        n = len(string)
        a = list(string)
        permute(a, 0, n-1)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testPermute']
    unittest.main()