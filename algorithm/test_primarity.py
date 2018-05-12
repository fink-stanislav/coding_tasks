
import unittest
from algorithm.primarity import is_prime


class TestPrimarity(unittest.TestCase):


    def test_is_prime(self):
        self.assertTrue(is_prime(1997))
        self.assertTrue(is_prime(2017))
        self.assertFalse(is_prime(1998))
        self.assertFalse(is_prime(2018))
        
        self.assertTrue(is_prime(1000000007))
        self.assertFalse(is_prime(100000003))
        self.assertTrue(is_prime(1000003))
        
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(16))
        self.assertFalse(is_prime(25))
        self.assertFalse(is_prime(36))
        self.assertFalse(is_prime(49))
        self.assertFalse(is_prime(64))
        self.assertFalse(is_prime(81))
        self.assertFalse(is_prime(100))
        self.assertFalse(is_prime(121))
        self.assertFalse(is_prime(144))
        self.assertFalse(is_prime(169))
        self.assertFalse(is_prime(196))
        self.assertFalse(is_prime(225))
        self.assertFalse(is_prime(256))
        self.assertFalse(is_prime(289))
        self.assertFalse(is_prime(324))
        self.assertFalse(is_prime(361))
        self.assertFalse(is_prime(400))
        self.assertFalse(is_prime(441))
        self.assertFalse(is_prime(484))
        self.assertFalse(is_prime(529))
        self.assertFalse(is_prime(576))
        self.assertFalse(is_prime(625))
        self.assertFalse(is_prime(676))
        self.assertFalse(is_prime(729))
        self.assertFalse(is_prime(784))
        self.assertFalse(is_prime(841))
        self.assertTrue(is_prime(907))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()