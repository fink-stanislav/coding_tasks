
class Node():
    def __init__(self, kind='regular'):
        self.children = {}  # mapping from character ==> Node
        self.kind = kind

def find(node, key):
    # Tree traverse should be used
    seen = {}
    for char in key:
        if char in node.children:
            seen[char] = [node]
            node = node.children[char]
        else:
            return 0

    return traverse1(node, 1, seen)

def traverse1(node, words, seen):
    if len(node.children) == 0:
        return words
    else:
        keys = list(node.children.keys())
        if words < len(keys):
            words = len(keys)
            
        if node.kind == 'terminal':
            words += 1

        next_node = node.children[keys[0]]
        for key in node.children.keys():
            try:
                nodes = seen[key]
                if next_node in nodes:
                    next_node = node.children[key]
                else:
                    seen[key] = [next_node]
                    return traverse1(next_node, words, seen)
            except:
                seen[key] = [next_node]
                return traverse1(next_node, words, seen)

        return words

def insert(root, string):
    node = root
    index_last_char = None
    for index_char, char in enumerate(string):
        if char in node.children:
            node = node.children[char]
        else:
            index_last_char = index_char
            break

    # append new nodes for the remaining characters, if any
    if index_last_char is not None: 
        for char in string[index_last_char:]:
            node.children[char] = Node()
            node = node.children[char]

    node.kind = 'terminal'
