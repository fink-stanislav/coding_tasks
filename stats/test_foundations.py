
import stats.foundations as fs
import unittest


class TestFoundations(unittest.TestCase):

    def test_median(self):
        arr = [64630, 11735, 14216, 99233, 14470, 4978, 73429, 38120, 51135, 67060]
        self.assertEqual(fs.median(arr), 44627.5)
    
    def test_median_1(self):
        arr = [3, 7, 8, 5, 12, 14, 21, 13, 18]
        self.assertEqual(fs.median(arr), 12)

    def test_mode(self):
        arr = [64630, 11735, 14216, 99233, 14470, 4978, 73429, 38120, 51135, 67060]
        self.assertEqual(fs.mode(arr), 4978)

    def test_weighted_mean(self):
        arr = [10, 40, 30, 50, 20]
        weights = [1, 2, 3, 4, 5]
        self.assertEqual(fs.weighted_mean(arr, weights), 32.0)
        
    def test_q1(self):
        arr = [3, 7, 8, 5, 12, 14, 21, 13, 18]
        self.assertEqual(fs.q1(arr), 6)
    
    def test_q3(self):
        arr = [3, 7, 8, 5, 12, 14, 21, 13, 18]
        self.assertEqual(fs.q3(arr), 16)

    def _iqr(self, numbers, freqs):
        unfolded = []
        for i in range(0, len(numbers)):
            number = numbers[i]
            addition = [number] * freqs[i]
            unfolded += addition
        return fs.iqr(unfolded)

    def test_iqr1(self):
        numbers = [6, 12, 8, 10, 20, 16]
        freqs = [5, 4, 3, 2, 1, 5]
        self.assertEqual(self._iqr(numbers, freqs), 9)

    def test_iqr0(self):
        numbers = [10, 40, 30, 50, 20]
        freqs = [1, 2, 3, 4, 5]
        self.assertEqual(self._iqr(numbers, freqs), 30)
        
    def test_q1_1(self):
        arr = [3, 7, 8, 5, 12, 14, 21, 15, 18, 14]
        self.assertEqual(fs.q1(arr), 7)

    def test_median_2(self):
        arr = [3, 7, 8, 5, 12, 14, 21, 15, 18, 14]
        self.assertEqual(fs.median(arr), 13)

    def test_q3_1(self):
        arr = [3, 7, 8, 5, 12, 14, 21, 15, 18, 14]
        self.assertEqual(fs.q3(arr), 15)

    def test_q1_2(self):
        arr = [4, 17, 7, 14, 18, 12, 3, 16, 10, 4, 4, 12]
        self.assertEqual(fs.q1(arr), 4)

    def test_median_3(self):
        arr = [4, 17, 7, 14, 18, 12, 3, 16, 10, 4, 4, 12]
        self.assertEqual(fs.median(arr), 11)

    def test_q3_2(self):
        arr = [4, 17, 7, 14, 18, 12, 3, 16, 10, 4, 4, 12]
        self.assertEqual(fs.q3(arr), 15)

    def test_is_int(self):
        self.assertTrue(fs.is_int(6.0))
        self.assertTrue(fs.is_int(12.0))
        self.assertTrue(fs.is_int(16.0))

    def test_cumulative_probability_at_least_1(self):
        x, n, p = 3, 6, 1.09 / (1 + 1.09)
        kind = 'at_least'
        b = fs.cumulative_probability(n, x, p, kind=kind)
        self.assertEqual(round(b, 3), 0.696)
     
    def test_cumulative_probability_at_most(self):
        x, n, p = 2, 10, 0.12
        kind = 'at_most'
        b = fs.cumulative_probability(n, x, p, kind=kind)
        self.assertEqual(round(b, 3), 0.891)

    def test_cumulative_probability_at_least_2(self):
        x, n, p = 2, 10, 0.12 
        kind = 'at_least'
        b = fs.cumulative_probability(n, x, p, kind=kind)
        self.assertEqual(round(b, 3), 0.342)

    def test_geometric_distribution(self):
        n, p = 5, 1./3
        g = fs.geometric_distribution(n, p)
        self.assertEqual(round(g, 3), 0.066)

    def test_poisson_distribution(self):
        average, desired = 2.5, 5
        p = fs.poisson_distribution(average, desired)
        self.assertEqual(round(p, 3), 0.067)

    def test_cor(self):
        seq1 = [10, 9.8, 8, 7.8, 7.7, 7, 6, 5, 4, 2]
        seq2 = [200, 44, 32, 24, 22, 17, 15, 12, 8, 4]

        cor = fs.cor(seq1, seq2)
        self.assertEqual(round(cor, 3), 0.612)

    def test_scor(self):
        seq1 = [10, 9.8, 8, 7.8, 7.7, 1.7, 6, 5, 1.4, 2]
        seq2 = [200, 44, 32, 24, 22, 17, 15, 12, 8, 4]

        scor = fs.scor(seq1, seq2)
        self.assertEqual(round(scor, 3), 0.903)

    def test_linear_regression(self):
        X = [95, 85, 80, 70, 60]
        Y = [85, 95, 70, 65, 70]
        b = fs.find_b(X, Y)
        a = fs.find_a(b, X, Y)

        actual = round(fs.linear_func(a, b, 80), 3)
        self.assertEqual(actual, 78.288)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()