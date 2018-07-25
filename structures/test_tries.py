
import unittest
from structures.tries import Node, insert, find
import os


def run(case_name):
    base_path = os.path.join('test_resources', 'tries')
    test_case_path = os.path.join(base_path, 'test_data_{}.txt'.format(case_name))

    inps = [line.rstrip('\n') for line in open(test_case_path)]

    trie = Node()

    found = []

    for inp in inps:
        opContact = inp.split()

        op = opContact[0]

        contact = opContact[1]

        if op == 'add':
            insert(trie, contact)
        elif op == 'find':
            found.append(find(trie, contact))

    test_result_path = os.path.join(base_path, 'test_results_actual_{}.txt'.format(case_name))
    with open(test_result_path.format(case_name), 'w') as actual:
        for f in found:
            actual.write(str(f))
            actual.write('\n')


class TestTries(unittest.TestCase):

    def _test(self, case_name):
        run(case_name)
        base_path = os.path.join('test_resources', 'tries')

        test_result_actual_path = os.path.join(base_path, 'test_results_actual_{}.txt'.format(case_name))
        actual = [line.rstrip('\n') for line in open(test_result_actual_path)]

        test_result_expected_path = os.path.join(base_path, 'test_results_expected_{}.txt'.format(case_name))
        expected = [line.rstrip('\n') for line in open(test_result_expected_path)]

        self.assertListEqual(actual, expected)

    def test_trie_4(self):
        self._test(4)

    def test_trie_11(self):
        self._test(11)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()