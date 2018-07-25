
import unittest

import matrices.matrix_operations as m

class TestMatrixOperations(unittest.TestCase):


    def test_rotate(self):
        # Driver Code
        N = 4
        v = 0
        row = []
        for x in range(N):
            col = []
            for y in range(N):
                col.append(v)
                v += 1
            row.append(col)
        
        mat = row

        m.rotate_matrix(mat)
        m.display_matrix(mat)

        m.rotate_matrix(mat)
        m.display_matrix(mat)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()