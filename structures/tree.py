# Recursive Python program for level order traversal of Binary Tree
 
class Node:

    def __init__(self, key):
        self.data = key 
        self.left = None
        self.right = None

# Breath first search/traversal
def bfs(root, func):
    h = height(root)
    for i in range(1, h+1):
        access_tree_level(root, i, func)
 
 
# Print nodes at a given level
def access_tree_level(root, level, func):
    if root is None:
        return
    if level == 1:
        func(root.data)
    elif level > 1:
        access_tree_level(root.left, level - 1, func)
        access_tree_level(root.right, level - 1, func)

""" Compute the height of a tree--the number of nodes
    along the longest path from the root node down to
    the farthest leaf node
"""
def height(node):
    if node is None:
        return 0
    else :
        # Compute the height of each subtree 
        lheight = height(node.left)
        rheight = height(node.right)

        #Use the larger one
        if lheight > rheight :
            return lheight+1
        else:
            return rheight+1

# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
def func(data):
    print(data)
 
bfs(root, func)