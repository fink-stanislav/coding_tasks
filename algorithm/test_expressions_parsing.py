
import unittest

import algorithm.expressions_parsing as ep

class TestParsing(unittest.TestCase):


    def test_is_valid(self):
        bv = ep.BraketsValidator()

        self.assertTrue  (bv.is_valid('{[()]}'))
        self.assertFalse (bv.is_valid('{[(])}'))
        self.assertTrue  (bv.is_valid('{{[[(())]]}}'))
        self.assertTrue  (bv.is_valid('()(())'))
        self.assertTrue  (bv.is_valid('[()(())]'))
        self.assertFalse (bv.is_valid(']'))
        self.assertFalse (bv.is_valid('['))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()