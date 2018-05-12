
import unittest
from algorithm.parsing import is_matched


class TestParsing(unittest.TestCase):


    def test_is_matched(self):
        self.assertTrue(is_matched('{[()]}'))
        self.assertFalse(is_matched('{[(])}'))
        self.assertTrue(is_matched('{{[[(())]]}}'))
        self.assertTrue(is_matched('()(())'))
        self.assertTrue(is_matched('[()(())]'))
        self.assertFalse(is_matched(']'))
        self.assertFalse(is_matched('['))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()