
"""
Consider a staircase of size n=4:

   #
  ##
 ###
####

Observe that its base and height are both equal to n, and the image is drawn using # symbols and spaces.
The last line is not preceded by any spaces.

"""

def count(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    return count(n - 1) + count(n - 2) + count(n - 3)

def non_recursive_count(n):
    seq = [1, 1, 2]

    if n <= 2:
        return seq[n]

    count = 2
    result = 0
    while count < n:
        result = sum(seq)
        seq.pop(0)
        seq.append(result)
        count += 1

    return result