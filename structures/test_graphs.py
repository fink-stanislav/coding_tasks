
import unittest
from structures.graphs import get_adjacent_nodes, create_graph, dfs


class TestGraphs(unittest.TestCase):


    def test_get_adjacent_nodes(self):
        grid = [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0], [1, 0, 0, 0]]
        result = get_adjacent_nodes(grid, 0, 0)
        self.assertListEqual(result, [(0, 1), (1, 1)])

    def test_create_graph(self):
        grid = [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0], [1, 0, 0, 0]]
        result = create_graph(grid)
        print result

    def test_dfs(self):
        grid = [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0], [1, 0, 0, 0]]
        result = create_graph(grid)
        self.assertEqual(dfs(result), 5)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()