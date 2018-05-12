
import unittest
from algorithm.structures import BinaryTree, Node, BinarySearchTree, Graph,\
    NonRecBST


class TestStructures(unittest.TestCase):


    def test_tree(self):
        tree = BinaryTree('D')
        tree.root.left = Node('B')
        tree.root.left.left = Node('A')
        tree.root.left.right = Node('C')

        tree.root.right = Node('E')
        tree.root.right.right = Node('F')

        self.assertTrue(tree.search('B'))
        self.assertFalse(tree.search('G'))
        self.assertEqual(tree.print_tree_preorder(), 'D-B-A-C-E-F')
        self.assertEqual(tree.print_tree_postorder(), 'A-C-B-F-E-D')
        self.assertEqual(tree.print_tree_inorder(), 'A-B-C-D-E-F')

    def test_bst(self):
        # Set up tree
        tree = BinarySearchTree(4)
        
        # Insert elements
        tree.insert(2)
        tree.insert(1)
        tree.insert(3)
        tree.insert(5)
        
        # Check search
        self.assertTrue(tree.search(4))
        self.assertTrue(tree.search(2))
        self.assertTrue(tree.search(1))
        self.assertTrue(tree.search(3))
        self.assertTrue(tree.search(5))
        self.assertFalse(tree.search(6))
        self.assertFalse(tree.search(0))
        
    def test_graph(self):
        graph = Graph()
        graph.insert_node(0)
        graph.insert_edge(100, 1, 2)
        graph.insert_edge(101, 1, 3)
        graph.insert_edge(102, 1, 4)
        graph.insert_edge(103, 3, 4)
        self.assertListEqual([(100, 1, 2), (101, 1, 3), (102, 1, 4), (103, 3, 4)], graph.get_edge_list()) 
        self.assertListEqual(graph.get_adjacency_list(),
                             [None, [(2, 100), (3, 101), (4, 102)], None, [(4, 103)], None])
        self.assertListEqual(graph.get_adjacency_matrix(),
                             [[0, 0, 0, 0, 0], [0, 0, 100, 101, 102], [0, 0, 0, 0, 0], [0, 0, 0, 0, 103], [0, 0, 0, 0, 0]])


    def test_non_rec_bst(self):
        tree = NonRecBST(5)
        tree.insert(4)
        tree.insert(2)
        tree.insert(1)
        tree.insert(3)
        tree.in_order_traverse()
            
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()