
from operator import xor

def xoring(arr):
    _sum = 0
    for a in arr:
        _sum = xor(_sum, a)

    return _sum
def count(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    if n == 4:
        return 7
    if n == 5:
        return 13
    return count(n - 1) + count(n - 2) + count(n - 3)

s = int(input().strip())
for a0 in range(s):
    n = int(input().strip())
    print(count(n))
