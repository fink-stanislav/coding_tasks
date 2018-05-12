
import operator
import math

def is_int(value):
    if value == round(value):
        return True

def mean(arr):
    _sum = sum(arr)
    _len = len(arr)
    return float(_sum) / _len

def middle(arr):
    _len = len(arr)
    middle1 = len(arr) // 2
    middle2 = middle1
    if _len % 2 == 0:
        middle2 = middle1 - 1
    return middle1, middle2

def median(arr):
    arr = sorted(arr)
    middle1, middle2 = middle(arr)
    return mean([arr[middle1], arr[middle2]])

def upper(arr):
    _, middle2 = middle(arr)
    middle2 += 1
    return arr[middle2:len(arr)]

def lower(arr):
    middle1, _ = middle(arr)
    return arr[0:middle1]

def q1(arr):
    arr = sorted(arr)
    return median(lower(arr))

def q3(arr):
    arr = sorted(arr)
    return median(upper(arr))

def iqr(arr):
    return q3(arr) - q1(arr)

def dev(arr):
    _mean = mean(arr)
    devs = [(v - _mean) ** 2 for v in arr]
    devs = float(sum(devs)) / len(devs)
    return math.sqrt(devs)

def mode(arr):
    counts = {}
    for a in arr:
        if a in counts:
            counts[a] += 1
        else:
            counts[a] = 1
    _max = max(counts.iteritems(), key=operator.itemgetter(1))[1]
    
    maxes = []
    for number, count in counts.iteritems():
        if count == _max:
            maxes.append(number)
    
    return min(maxes)

def weighted_mean(arr, weights):
    weighted = []
    for i in range(0, len(arr)):
        wi = weights[i]
        ai = arr[i]
        weighted.append(wi * ai)
    weighted = sum(weighted)
    w_sum = sum(weights)
    return float(weighted) / w_sum

def combination(n, x):
    return float(math.factorial(n)) / (math.factorial(x) * math.factorial(n - x))

def binomial_distribution(n, x, p):
    """
    @param n: total number of trials
    @param x: number of successes
    @param p: probability of success
    """
    return combination(n, x) * p ** x * (1 - p) ** (n - x)

def cumulative_probability(n, x, p, kind='at_least'):
    b = 0
    if kind == 'at_least':
        for i in range(x, n + 1):
            b += binomial_distribution(n, i, p)
    elif kind == 'at_most':
        for i in range(0, x + 1):
            b += binomial_distribution(n, i, p)
    else:
        return None
    return b

def geometric_distribution(n, p):
    '''
    @param n: total number of trials
    @param p: probability of success of trial
    '''
    return ((1 - p) ** (n - 1)) * p

def poisson_distribution(average, desired):
    v1 = average ** desired
    v2 = math.e ** (- average)
    return v1 * v2 / math.factorial(desired)

def normal_pdf(x, mean, stdev):
    return 0.5 * (1 + math.erf((x - mean)/math.sqrt(2 * stdev**2)))

def normal_sample_mean(sample_size, sample_mean):
    return sample_mean * sample_size

def normal_sample_dev(sample_size, sample_dev):
    return (sample_size ** 0.5) * sample_dev

def L(m, z, d, n=1):
    return m - (z * d) / (n ** 0.5)

def U(m, z, d, n=1):
    return m + (z * d) / (n ** 0.5)

def cov(seq1, seq2):
    n1 = len(seq1)
    n2 = len(seq2)
    if n1 != n2:
        return None
    result = 1.0 / n1
    m1 = mean(seq1)
    m2 = mean(seq2)
    
    d1 = [v - m1 for v in seq1]
    d2 = [v - m2 for v in seq2]
    mul = [_d1 * _d2 for _d1, _d2 in zip(d1, d2)]
    result = result * sum(mul)
    return result

def cor(seq1, seq2):
    return cov(seq1, seq2) / (dev(seq1) * dev(seq2))

def calc_ranks(seq):
    sorted_seq = sorted(seq)
    ranks = [sorted_seq.index(v) for v in seq]
    return ranks

def scor(seq1, seq2):
    ranks1 = calc_ranks(seq1)
    ranks2 = calc_ranks(seq2)
    return cor(ranks1, ranks2)

# Linear Regression
def find_a(b, X, Y):
    x = mean(X)
    y = mean(Y)
    return y - b * x

def find_b(X, Y):
    _cor = cor(X, Y)
    dev_x = dev(X)
    dev_y = dev(Y)
    return _cor * (dev_y / dev_x)

def linear_func(a, b, x):
    return a + b * x
