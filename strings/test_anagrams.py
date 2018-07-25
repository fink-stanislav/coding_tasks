
import unittest
from strings.anagrams import count


class TestAnagrams(unittest.TestCase):


    def test_anagrams(self):
        actual = count('fcrxzwscanmligyxyvym', 'jxwtrhvujlmrpdoqbisbwhmgpmeoke')
        self.assertEqual(actual, 30)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_anagrams']
    unittest.main()