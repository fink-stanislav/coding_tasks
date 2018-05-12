

# Question 1 ####################################
def count_letters(string):
    _from = ord('A')
    _to = ord('z')
    counts = {}
    for a in string:
        if ord(a) >= _from and ord(a) <= _to:
            if a in counts:
                counts[a] += 1
            else:
                counts[a] = 1
    return counts

def count_particular_letter(s, letter):
    count = 0
    for a in s:
        if a == letter:
            count += 1
    return count

def question1(s, t):
    if s is None or t is None:
        return False

    if not isinstance(s, basestring) or not isinstance(t, basestring):
        return False

    if len(t) == 0:
        return True 

    t_count = count_letters(t)
    for t_letter in t:
        cnt = count_particular_letter(s, t_letter)
        if cnt < t_count[t_letter]:
            return False

    return True

def question1_test1():
    print question1('lorem ipsum dolor sit amet', 'ips')
    # True

def question1_test2():
    print question1('lorem ipsum dolor sit amet', 'tis')
    # False

def question1_test3():
    print question1(None, '')
    # False

def question1_test4():
    print question1('', None)
    # False


# Question 2 ####################################
def build_palindrome(stack, middle_char=None):
    string = []
    if middle_char is not None:
        string.append(middle_char)
    while len(stack) > 0:
        popped = stack.pop()
        string.insert(0, popped)
        string.append(popped)
    return ''.join(string)

def find_palindrome(string, index, result=None):
    if len(string) <= index:
        return result
    letter = string[index]
    last_index = string.rfind(letter, index + 1)
    if last_index > 0:
        length = last_index - index + 1

        has_middle_char = False
        if length % 2 != 0:
            has_middle_char = True

        radius = length // 2

        palindrome = []
        for i in range(0, radius):
            first = string[i + index]
            last = string[index + length - i - 1]
            if first == last:
                palindrome.append(first)
            else:
                return find_palindrome(string, i + index, result=result)

        middle_char = None
        if has_middle_char:
            middle_char = string[radius + index]
        palindrome = build_palindrome(palindrome, middle_char=middle_char)

        if result is None or (len(palindrome) > len(result)):
            return find_palindrome(string, last_index + 1, result=palindrome)
        else:
            return find_palindrome(string, last_index + 1, result=result)

    else:
        return find_palindrome(string, index + 1, result=result)

def question2(a):
    if a is None:
        return None

    if not isinstance(a, basestring):
        return None

    if len(a) <= 1:
        return a

    return find_palindrome(a, 0)

def question2_test1():
    print question2(None)
    # None
    
def question2_test2():
    print question2('a')
    # a

def question2_test3():
    print question2('cac bvnvb')
    # bvnvb

def question2_test4():
    print question2('qaaabbcbbaaa')
    # aaabbcbbaaa

def question2_test5():
    print question2('abceqrvrba')
    # rvr

# Question 3 ####################################
class Vertex(object):
    def __init__(self, name):
        self.name = name
        self.edges = []

    def connect(self, other_vertex, weight):
        edge = Edge(self.name, other_vertex.name, weight)
        self.edges.append(edge)
        other_vertex.edges.append(edge)
        return other_vertex

class Edge(object):
    def __init__(self, _from, _to, weight):
        self.weight = weight
        self._from = _from
        self._to = _to

class DisjointSets(object):
    def __init__(self, names):
        self.sets = []
        for name in names:
            self.sets.append(set(name))

    def find_set(self, s):
        for index, _set in enumerate(self.sets):
            if len(_set & s) > 0:
                return index, _set
        return None

    def join(self, s1, i1, s2, i2):
        s = s1 | s2
        self.sets[i1] = s
        del self.sets[i2]

class Graph(object):
    def __init__(self):
        self.vertices = []

    def adj_dict(self):
        result = {}
        for vertex in self.vertices:
            edges = []
            for edge in vertex.edges:
                name = edge._to
                if name == vertex.name:
                    name = edge._from
                edges.append((name, edge.weight))
            result[vertex.name] = edges
        return result

    def _get_vertex(self, vertex_name):
        for vertex in self.vertices:
            if vertex.name == vertex_name:
                return vertex
        return None

    def edges_list(self):
        result = []
        adj = self.adj_dict()
        for vertex_name, edges in adj.iteritems():
            for edge in edges:
                tpl = (vertex_name, edge[0], edge[1])
                result.append(tpl)
        return result

    def connect(self, vertex_name1, vertex_name2, weight):
        v1 = self._get_vertex(vertex_name1)
        if v1 is None:
            v1 = Vertex(vertex_name1)
            self.vertices.append(v1)
        v2 = self._get_vertex(vertex_name2)
        if v2 is None:
            v2 = Vertex(vertex_name2)
            self.vertices.append(v2)
        v1.connect(v2, weight)

    def min_tree(self):
        edges = self.edges_list()
        edges = sorted(edges, key = lambda item: item[2])        

        tree = Graph()

        names = [v.name for v in self.vertices]
        sets = DisjointSets(names)

        for edge in edges:
            v1 = edge[0]
            v2 = edge[1]

            i1, s1 = sets.find_set(set(v1))
            i2, s2 = sets.find_set(set(v2))

            if len(s1 & s2) == 0:
                sets.join(s1, i1, s2, i2)
                tree.connect(v1, v2, edge[2])

        return tree

def question3(G):
    if G is None:
        return None
    adj_dict = G.min_tree().adj_dict()
    return adj_dict

def question3_test1():
    print question3(None)
    # None

def question3_test2():
    print question3(Graph())
    # {}

def question3_test3():
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
    print question3(g)
    # {'A': [('B', 2)], 'C': [('B', 1)], 'B': [('C', 1), ('A', 2), ('K', 2)], 'E': [('K', 1), ('I', 1), ('J', 2), ('D', 3)], 'D': [('E', 3)], 'I': [('E', 1)], 'K': [('E', 1), ('B', 2), ('M', 3)], 'J': [('E', 2)], 'M': [('K', 3)]}


# Question 4 ####################################
def get_parent(T, n, r):
    if n == r:
        return r
    return [i for i in range(0, len(T)) if T[i][n] == 1][0]

def get_equal_parent(parents):
    result = set([x for x in parents if parents.count(x) > 1])
    if len(result) > 0:
        return result.pop()
    return None

def find_parents(T, r, n1, n2, parents):
    p1 = get_parent(T, n1, r)
    p2 = get_parent(T, n2, r)

    parents.append(p1)
    parents.append(p2)

    common_parent = get_equal_parent(parents)

    if common_parent is not None:
        return common_parent

    return find_parents(T, r, p1, p2, parents)

def question4(T, r, n1, n2):
    if T is None or r is None or n1 is None or n2 is None:
        return None
    if len(T) == 0:
        return None
    return find_parents(T, r, n1, n2, [])

def question4_test1():
    print question4(None, 1, 1, 1)
    # None

def question4_test2():
    print question4([], 1, 2, 3)
    # None

def question4_test3():
    T = [[0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [1, 0, 0, 0, 1],
         [0, 0, 0, 0, 0]]

    print question4(T, 3, 1, 4)
    # 3

def question4_test4():
    T = [[0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 1],
         [0, 0, 1, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0],
         [1, 0, 0, 0, 0, 0, 0]]

    print question4(T, 5, 0, 1)
    # 2

# Question 5 ####################################
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self, data):
        self.root = Node(data)
        self.l = 1

    def append(self, data):
        current = self.root
        while current.next is not None:
            current = current.next
        current.next = Node(data)
        self.l += 1

    def length(self):
        return self.l

    def find(self, count=0):
        _length = self.length()
        position = _length - count + 1

        counter = 1
        current = self.root
        while current is not None:
            if counter == position:
                return current.data
            current = current.next
            counter += 1
        return None

def question5(ll, m):
    if ll is None or m is None:
        return None
    return ll.find(count=m)

def _create_list():
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    return ll

def question5_test1():
    ll = _create_list()
    print question5(ll, 2)
    # 4

def question5_test2():
    print question5(None, 1)
    # None

def question5_test3():
    print question5(LinkedList(None), None)
    # None

def question5_test4():
    print question5(LinkedList(None), 1)
    # None

def question5_test5():
    ll = _create_list()
    print question5(ll, 10)
    # None    

if __name__ == "__main__":
    print 'Question 1'
    question1_test1()
    question1_test2()
    question1_test3()
    question1_test4()

    print 'Question 2'
    question2_test1()
    question2_test2()
    question2_test3()
    question2_test4()
    question2_test5()

    print 'Question 3'
    question3_test1()
    question3_test2()
    question3_test3()

    print 'Question 4'
    question4_test1()
    question4_test2()
    question4_test3()
    question4_test4()

    print 'Question 5'
    question5_test1()
    question5_test2()
    question5_test3()
    question5_test4()
    question5_test5()
