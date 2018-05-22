
import unittest
from structures.queues import MyQueue


class TestQueues(unittest.TestCase):


    def test_queue(self):
        q = MyQueue()
        q.put(42)
        q.pop()
        q.put(14)
        self.assertEqual(q.peek(), 14)
        q.put(28)
        self.assertEqual(q.peek(), 14)
        q.put(60)
        q.put(78)
        q.pop()
        q.pop()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()