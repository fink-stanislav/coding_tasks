
import unittest

import solutions as sl
from udacity.solutions import LinkedList, Graph

class TestSolutions(unittest.TestCase):

    #############################################
    def test_question1_edge_cases(self):
        self.assertFalse(sl.question1(None, None))
        self.assertFalse(sl.question1(None, ''))
        self.assertFalse(sl.question1('', None))
        self.assertTrue(sl.question1('', ''))
        self.assertFalse(sl.question1('', 1))
        self.assertFalse(sl.question1(1, ''))

    def test_question1_common_cases(self):
        self.assertTrue(sl.question1('udacity', 'ci'))
        self.assertFalse(sl.question1('udacity', 'Ci'))
        self.assertTrue(sl.question1('dolor', 'lordo'))
        self.assertTrue(sl.question1('sit', 'tis'))
        self.assertTrue(sl.question1('udacity', 'tiyc'))

    #############################################
    def test_question2_edge_cases(self):
        self.assertIsNone(sl.question2(None))
        self.assertEqual(sl.question2(''), '')
        self.assertEqual(sl.question2('a'), 'a')
        self.assertIsNone(sl.question2(1))

    def test_question2_common_cases(self):
        self.assertEqual(sl.question2('abccba'), 'abccba')
        self.assertEqual(sl.question2('qaaabbcbbaaa'), 'aaabbcbbaaa')
        self.assertEqual(sl.question2('zabccbaw'), 'abccba')
        self.assertEqual(sl.question2('aaqwlwq'), 'qwlwq')
        self.assertEqual(sl.question2('cacqbvnvb'), 'bvnvb')
        self.assertEqual(sl.question2('cac bvnvb'), 'bvnvb')
        self.assertIsNone(sl.question2('abc'))
        self.assertEqual(sl.question2('abceqrvrba'), 'rvr')

    def test_build_palindrome(self):
        self.assertEqual(sl.build_palindrome(['a', 'b', 'c']), 'abccba')
        self.assertEqual(sl.build_palindrome(['a', 'b'], middle_char='c'), 'abcba')

    #############################################
    def _get_graph(self):
        g = Graph()
        g.connect('A', 'B', 2)
        g.connect('B', 'C', 1)
        g.connect('B', 'K', 2)
        g.connect('D', 'C', 5)
        g.connect('B', 'E', 6)
        g.connect('K', 'E', 1)
        g.connect('E', 'D', 3)
        g.connect('D', 'J', 4)
        g.connect('J', 'E', 2)
        g.connect('E', 'I', 1)
        g.connect('I', 'K', 2)
        g.connect('K', 'M', 3)
        return g

    def test_build_graph(self):        
        g = self._get_graph()
        adj_dict = g.adj_dict()

        self.assertListEqual(adj_dict['A'], [('B', 2)])
        self.assertListEqual(adj_dict['C'], [('B', 1), ('D', 5)])
        self.assertListEqual(adj_dict['B'], [('A', 2), ('C', 1), ('K', 2), ('E', 6)])
        self.assertListEqual(adj_dict['E'], [('B', 6), ('K', 1), ('D', 3), ('J', 2), ('I', 1)])
        self.assertListEqual(adj_dict['D'], [('C', 5), ('E', 3), ('J', 4)])
        self.assertListEqual(adj_dict['I'], [('E', 1), ('K', 2)])
        self.assertListEqual(adj_dict['K'], [('B', 2), ('E', 1), ('I', 2), ('M', 3)])
        self.assertListEqual(adj_dict['J'], [('D', 4), ('E', 2)])
        self.assertListEqual(adj_dict['M'], [('K', 3)])

    def test_question3(self):
        g = self._get_graph()
        adj_dict = sl.question3(g)

        self.assertListEqual(adj_dict['A'], [('B', 2)])
        self.assertListEqual(adj_dict['C'], [('B', 1)])
        self.assertListEqual(adj_dict['B'], [('C', 1), ('A', 2), ('K', 2)])
        self.assertListEqual(adj_dict['E'], [('K', 1), ('I', 1), ('J', 2), ('D', 3)])
        self.assertListEqual(adj_dict['D'], [('E', 3)])
        self.assertListEqual(adj_dict['I'], [('E', 1)])
        self.assertListEqual(adj_dict['K'], [('E', 1), ('B', 2), ('M', 3)])
        self.assertListEqual(adj_dict['J'], [('E', 2)])
        self.assertListEqual(adj_dict['M'], [('K', 3)])

    def test_question3_edge_cases(self):
        self.assertIsNone(sl.question3(None))
        self.assertDictEqual(sl.question3(Graph()), {})

    #############################################
    def test_question4_given_test_case(self):
        T = [[0, 1, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [1, 0, 0, 0, 1],
             [0, 0, 0, 0, 0]]

        self.assertEqual(sl.question4(T, 3, 1, 4), 3)
        self.assertEqual(sl.question4(T, 3, 4, 1), 3)
        self.assertEqual(sl.question4(T, 3, 4, 0), 3)
    
    def test_question4_custom1(self):
        T = [[0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [1, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 1, 1, 0, 0]]

        self.assertEqual(sl.question4(T, 5, 1, 0), 2)
        self.assertEqual(sl.question4(T, 5, 0, 3), 5)
        self.assertEqual(sl.question4(T, 5, 4, 2), 5)
        self.assertEqual(sl.question4(T, 5, 1, 5), 5)
        self.assertEqual(sl.question4(T, 5, 0, 2), 5)
        self.assertEqual(sl.question4(T, 5, 4, 1), 5)

    def test_question4_custom2(self):
        T = [[0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 1, 0, 0, 0, 0, 1],
             [0, 0, 1, 0, 1, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 0],
             [1, 0, 0, 0, 0, 0, 0]]

        self.assertEqual(sl.question4(T, 5, 4, 0), 3)
        self.assertEqual(sl.question4(T, 5, 1, 4), 3)
        self.assertEqual(sl.question4(T, 5, 0, 1), 2)
        self.assertEqual(sl.question4(T, 5, 6, 4), 3)
        self.assertEqual(sl.question4(T, 5, 6, 2), 3)
        
    def test_question4_edge_cases(self):
        self.assertIsNone(sl.question4(None, 1, 1, 1))
        self.assertIsNone(sl.question4([], 1, 2, 3))

    #############################################
    def test_question5(self):
        ll = LinkedList(1)
        ll.append(2)
        ll.append(3)
        ll.append(4)
        ll.append(5)

        self.assertEqual(ll.length(), 5)
        self.assertEqual(sl.question5(ll, 1), 5)
        self.assertEqual(sl.question5(ll, 2), 4)
        self.assertEqual(sl.question5(ll, 3), 3)
        self.assertEqual(sl.question5(ll, 4), 2)
        self.assertEqual(sl.question5(ll, 5), 1)

    def test_question5_edge_cases(self):
        self.assertIsNone(sl.question5(None, 1))
        self.assertIsNone(sl.question5(LinkedList(None), None))
        self.assertIsNone(sl.question5(LinkedList(None), 1))

        ll = LinkedList(1)
        ll.append(2)
        ll.append(3)
        ll.append(4)
        ll.append(5)
        self.assertIsNone(sl.question5(ll, 10))
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
