
import unittest
    
def max_score(value, seq):
    _max = 0
    _i = -1
    for i, v in enumerate(seq):
        x = value ^ v
        if x > _max:
            _max = v
            _i = i + 1
    return _max, _i

# Complete the maximumElegance function below.
def maximumElegance(q, s, b):
    # Return an integer denoting the maximum elegance which can be obtained by Diane.
    if not b:
        return 0
    
    used = {}
    scores = []
    
    for i, _b in enumerate(b):
        if i not in used:
            _max, _i = max_score(_b, b[i + 1:])
            scores.append(_max)
            used[i] = True
            
    return sum(scores)

    
class Test(unittest.TestCase):


    def testName(self):
        print maximumElegance(None, None, [2,3,1])
    
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    