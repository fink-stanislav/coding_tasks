
import unittest
from pramp.decrypting import decrypt


class TestDecrypting(unittest.TestCase):


    def test_decrypt_1(self):
        actual = decrypt('dnotq')
        expected = 'crime'
        self.assertEqual(actual, expected)

    def test_decrypt_2(self):
        actual = decrypt('flgxswdliefy')
        expected = 'encyclopedia'
        self.assertEqual(actual, expected)

    def test_decrypt_3(self):
        actual = decrypt('rajsb')
        expected = 'qqqqq'
        self.assertEqual(actual, expected)
        
    def test_decrypt_4(self):
        actual = decrypt('bvqmjhgghjmqvbiqzjugthwmdv')
        expected = 'abcdefghijklmnopqrstuvwxyz'
        self.assertEqual(actual, expected)

    def test_decrypt_5(self):
        actual = decrypt('eobamwpnlmhklrq')
        expected = 'drugtrafficking'
        self.assertEqual(actual, expected)
        
    def test_decrypt_6(self):
        actual = decrypt('')
        expected = ''
        self.assertEqual(actual, expected)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()