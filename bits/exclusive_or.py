
from operator import xor

def xoring(arr):
    _sum = 0
    for a in arr:
        _sum = xor(_sum, a)

    return _sum

def swap_ints(a, b):
    a = xor(a, b)
    b = xor(a, b)
    a = xor(a, b)
    return a, b
