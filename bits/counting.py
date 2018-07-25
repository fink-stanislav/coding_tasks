# Python program to compute sum of pairwise bit differences
 
def sum_bit_diffs(arr):
    ans = 0  # Initialize result
    n = len(arr)
 
    # traverse over all bits
    for i in range(0, 32):
     
        # count number of elements with i'th bit set
        count = 0
        for j in range(0, n):
            if ( (arr[j] & (1 << i)) ):
                count+=1
 
        # Add "count * (n - count) * 2" to the answer
        ans += (count * (n - count) * 2);
     
    return ans
 
# Iterative Python3 program
# to compute modular power
 
# Iterative Function to calculate
# (x^y)%p in O(log y) 
def power(x, y, p) :
    res = 1     # Initialize result
 
    # Update x if it is more
    # than or equal to p
    x = x % p 
 
    while (y > 0) :
         
        # If y is odd, multiply
        # x with result
        if ((y & 1) == 1) :
            res = (res * x) % p
 
        # y must be even now
        y = y >> 1      # y = y/2
        x = (x * x) % p
         
    return res