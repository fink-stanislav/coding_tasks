
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        return self.preorder_search(self.root, find_val)

    def print_tree_preorder(self):
        return self.preorder_print(self.root, "")[:-1]

    def print_tree_postorder(self):
        return self.postorder_print(self.root, "")[:-1]

    def print_tree_inorder(self):
        return self.inorder_print(self.root, "")[:-1]

    def preorder_search(self, start, find_val):
        if start:
            if start.value == find_val:
                return True
            else:
                return self.preorder_search(start.left, find_val) or self.preorder_search(start.right, find_val)
        return False

    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        if start:
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

    def inorder_print(self, start, traversal):
        if start:
            traversal = self.preorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.right, traversal)
        return traversal

class BinarySearchTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def _insert(self, current, new_val, parent=None, left=True):
        if current is None:
            current = Node(new_val)
            if left:
                parent.left = current
            else:
                parent.right = current
            return
        if current.value > new_val:
            self._insert(current.right, new_val, parent=current, left=False)
        else:
            self._insert(current.left, new_val, parent=current)

    def insert(self, new_val):
        self._insert(self.root, new_val)

    def _search(self, current, find_val):
        if current is None:
            return False
        if current.value == find_val:
            return True
        else:
            if current.value > find_val:
                return self._search(current.right, find_val)
            else:
                return self._search(current.left, find_val)

    def search(self, find_val):
        return self._search(self.root, find_val)

class NonRecBST():
    def __init__(self, root):
        self.root = Node(root)

    def _insert(self, current, new_val, parent=None, left=True):
        if current is None:
            current = Node(new_val)
            if left:
                parent.left = current
            else:
                parent.right = current
            return
        if current.value > new_val:
            self._insert(current.right, new_val, parent=current, left=False)
        else:
            self._insert(current.left, new_val, parent=current)

    def insert(self, new_val):
        self._insert(self.root, new_val)

    def _in_order_traverse(self, current):
        stack = []
        done = False
        while not done:
            if current is None:
                if len(stack) > 0:
                    current = stack.pop()

                    print current.value

                    current = current.right
                else:
                    done = True
            else:
                stack.append(current)
                current = current.left


    def in_order_traverse(self):
        return self._in_order_traverse(self.root)

class GraphNode(object):
    def __init__(self, value):
        self.value = value
        self.edges = []

class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to

class Graph(object):
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    def insert_node(self, new_node_val):
        new_node = GraphNode(new_node_val)
        self.nodes.append(new_node)

    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        from_found = None
        to_found = None
        for node in self.nodes:
            if node_from_val == node.value:
                from_found = node
            if node_to_val == node.value:
                to_found = node
        if from_found == None:
            from_found = GraphNode(node_from_val)
            self.nodes.append(from_found)
        if to_found == None:
            to_found = GraphNode(node_to_val)
            self.nodes.append(to_found)
        new_edge = Edge(new_edge_val, from_found, to_found)
        from_found.edges.append(new_edge)
        to_found.edges.append(new_edge)
        self.edges.append(new_edge)

    def get_edge_list(self):
        """Don't return a list of edge objects!
        Return a list of triples that looks like this:
        (Edge Value, From Node Value, To Node Value)"""
        result = []
        for edge in self.edges:
            result.append((edge.value, edge.node_from.value, edge.node_to.value))
        return result

    def get_adjacency_list(self):
        """Don't return any Node or Edge objects!
        You'll return a list of lists.
        The indices of the outer list represent
        "from" nodes.
        Each section in the list will store a list
        of tuples that looks like this:
        (To Node, Edge Value)"""

        result = []
        for node in self.nodes:
            sublist = None
            for edge in node.edges:
                if edge.node_from.value == node.value:
                    tpl = (edge.node_to.value, edge.value)
                    if sublist is None:
                        sublist = []
                    sublist.append(tpl)
            result.append(sublist)
        return result

    def get_adjacency_matrix(self):
        """Return a matrix, or 2D list.
        Row numbers represent from nodes,
        column numbers represent to nodes.
        Store the edge values in each spot,
        and a 0 if no edge exists."""

        result = []
        adj_list = self.get_adjacency_list()
        for adj in adj_list:
            row = [0] * len(adj_list)
            if adj is not None:
                for connection in adj:
                    row[connection[0]] = connection[1]
            result.append(row)
        return result
