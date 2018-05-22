
class Graph(object):
    def __init__(self):
        self.nodes = []

    def get_node(self, _id):
        result = [node for node in self.nodes if node._id == _id]
        if len(result) > 0:
            return result[0]
        return None

    def add_node(self, node):
        self.nodes.append(node)

    def count_nodes(self, color='b'):
        counter = 0
        for node in self.nodes:
            if node.color == color:
                counter += 1
        return counter

    def repaint(self, initial_color='b', color='r'):
        for node in self.nodes:
            if node.color == initial_color:
                node.color = color

class Node(object):
    def __init__(self, _id):
        self._id = _id
        self.connections = set()
        self.i = _id[0]
        self.j = _id[1]
        self.color = 'w'

    def connect(self, _id):
        self.connections.add(_id)

    def connect_list(self, _ids):
        [self.connect(_id) for _id in _ids]

def get_adjacent_nodes(grid, i, j):
    rows = len(grid)
    cols = len(grid[0])

    rs = i - 1
    re = i + 1
    cs = j - 1
    ce = j + 1

    if i == 0:
        rs = i
    if j == 0:
        cs = j
    if i == rows - 1:
        re = i
    if j == cols - 1:
        ce = j

    nodes = []
    for _i in range(rs, re + 1):
        for _j in range(cs, ce + 1):
            if i == _i and j == _j:
                continue
            if grid[_i][_j] == 1:
                nodes.append((_i, _j))

    return nodes
    
def create_graph(grid):
    graph = Graph()
    
    rows = len(grid)
    cols = len(grid[0])
    
    for i in range(0, rows):
        for j in range(0, cols):
            if grid[i][j] == 1:
                _id = (i, j)
                node = graph.get_node(_id)
                if node is None:
                    node = Node(_id)
                adj = get_adjacent_nodes(grid, i, j)
                node.connect_list(adj)
                graph.add_node(node)

    return graph

def _dfs(graph, node):
    node.color = 'g'
    for adj in node.connections:
        adj_node = graph.get_node(adj)
        if adj_node.color == 'w':
            _dfs(graph, adj_node)
    node.color = 'b'

def dfs(graph):
    count = 0
    for node in graph.nodes:
        if node.color == 'w':
            _dfs(graph, node)
            c = graph.count_nodes()
            if c > count:
                count = c
            graph.repaint()
    return count
