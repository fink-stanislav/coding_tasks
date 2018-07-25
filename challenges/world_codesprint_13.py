
import unittest
from itertools import islice
import operator
import challenges.world_codesprint_13_helper as h

class TestSetOperations(unittest.TestCase):

    ##### 1
    def test_challenge_1(self):
        arr = [1, 2, 2, 3, 4, 5, 2, 8, 9, 10]
        _min = min(arr)
        _max = max(arr)
        required_set = set([i for i in range(_min, _max + 1)])
        actual_set = set(arr)
        diff = sorted(list(required_set - actual_set))
        string = ' '.join(str(x) for x in diff)
        self.assertEqual(string, '6 7')

    ##### 2
    def _mul(self, seq):
        return reduce(operator.mul, seq, 1)
    
    def window(self, seq, n=2):
        "Returns a sliding window (of width n) over data from the iterable"
        "   s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...                   "
        it = iter(seq)
        result = tuple(islice(it, n))
        if len(result) == n:
            yield result
        for elem in it:
            result = result[1:] + (elem,)
            yield result

    def is_good(self, seq, k, m):
        if 0 in seq:
            return 0 == k
        
        r = reduce(operator.mul, seq, 1)
        return r % m == k

    def count_good(self, arr, k, m):
        arr = [s % m for s in arr]
        counter = 0
        l = len(arr)
        for i in range(1, l + 1):
            
            start = 0
            end = i
            
            while end <= l:
                counter += self.is_good(arr[start:end], k, m)
                start += 1
                end += 1
            
        return counter

    def test_challenge_2(self):
        arr = [1, 10, 10]
        self.assertEqual(self.count_good(arr, 1, 11), 3)
        arr = [1, 0, 3, 0, 4]
        self.assertEqual(self.count_good(arr, 0, 3), 13)
        arr = [2, 2, 2, 2, 2]
        self.assertEqual(self.count_good(arr, 2, 3), 9)

    ##### 3
    
    def initialize(self, _students, _requests):
        students = []
        for st in _students:
            student = st.split(' ')
            result = {'names': set()}
            result['names'].add(student[0])
            grade = int(student[1])
            result['grades'] = {grade: 1}
            students.append(result)
        
        h.groups = students
    
        requests = []
        for r in _requests:
            request = r.split(' ')
            request = {'from': request[0], 'to': request[1]}
            requests.append(request)
        return students, requests
    
    def test_membersInTheLargestGroups1(self):
        a = 2
        b = 3
        f = 2
        s = 2
        t = 2
        students = ['A 1', 'B 2', 'C 3', 'D 1', 'E 2']
        requests = ['A B', 'B A', 'C D', 'E D', 'E A', 'B D', 'B C']
        
                
        h.membersInTheLargestGroups(a, b, f, s, t, students, requests)

    def test_membersInTheLargestGroups2(self):
        a = 5
        b = 5
        f = 2
        s = 2
        t = 2
        students = ['A 1', 'B 2', 'C 3', 'D 1', 'E 2', 'F 1', 'G 1']
        requests = ['A B', 'B C', 'D E', 'C A', 'C B', 'F A', 'G A']
        
        
        h.membersInTheLargestGroups(a, b, f, s, t, students, requests)

    def test_membersInTheLargestGroups3(self):
        a = 2
        b = 9
        f = 9
        s = 9
        t = 9
        students = ['Hulk 2', 'BlackWidow 2', 'IronMan 2', 'Thor 3', 'SpiderMan 1']
        requests = ['Hulk Thor', 'IronMan SpiderMan', 'Hulk Thor', 'Hulk Thor', 'Hulk Thor']
        
        
        h.membersInTheLargestGroups(a, b, f, s, t, students, requests)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()