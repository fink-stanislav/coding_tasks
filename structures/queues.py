
class MyQueue(object):
    def __init__(self):
        self.first = []
        self.second = []
    
    def peek(self):
        len1 = len(self.first)
        len2 = len(self.second)
        if len1 == 0 and len2 == 0:
            return None
        if len1 > 0:
            return self.first[0]
        if len2 > 0:
            return self.second[0]

    def pop(self):
        for _ in range(0, len(self.first)):
            self.second.append(self.first.pop(0))
        return self.second.pop(0)

    def put(self, value):
        for _ in range(0, len(self.second)):
            self.first.append(self.second.pop(0))
        self.first.append(value)

class MyQueueFast(object):
    def __init__(self):
        self.q = []
    
    def peek(self):
        if len(self.q) > 0:
            return self.q[0]
        return None

    def pop(self):
        if len(self.q) > 0:
            return self.q.pop(0)
        return None

    def put(self, value):
        self.q.append(value)
