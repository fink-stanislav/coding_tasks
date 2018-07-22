import copy
    
def swap(a, i, j):
    if len(a) > 1:
        temp = a[i]
        a[i] = a[j]
        a[j] = temp

def bubble_sort(arr):
    n = len(arr)
    while True:
        swapped = False
        for i in range(1, n):
            if arr[i - 1] > arr[i]:
                swap(arr, i - 1, i)
                print(arr)
                swapped = True
        if not swapped:
            break
        n -= 1
    return arr

# Quick sort
def quick_sort(A, lo, hi):
    if lo < hi:
        p = partition(A, lo, hi)
        quick_sort(A, lo, p - 1)
        quick_sort(A, p + 1, hi)
    return A

def partition(A, lo, hi):
    pivot = A[lo]
    i = lo + 1 #left
    j = hi #right
    done = False
    while not done:
        while A[i] <= pivot and i <= j:
            i += 1

        while A[j] >= pivot and i <= j:
            j -= 1

        if j < i:
            done = True
        else:
            swap(A, i, j)
    swap(A, lo, j)
    return j

# Mergesort recursive
def _merge(a, aux, lo, mid, hi):
    for k in range(lo, hi + 1):
        aux[k] = a[k]

    i = lo
    j = mid + 1

    for k in range(lo, hi + 1):
        if i > mid:
            a[k] = aux[j]
            j += 1
        elif j > hi:
            a[k] = aux[i]
            i += 1
        elif aux[j] < aux[i]:
            a[k] = aux[j]
            j += 1
        else:
            a[k] = aux[i]
            i += 1

def _merge_sort_rec(a, aux, lo, hi):
    if hi <= lo:
        return
    mid = lo + (hi - lo) / 2
    _merge_sort_rec(a, aux, lo, mid)
    _merge_sort_rec(a, aux, mid+1, hi)
    _merge(a, aux, lo, mid, hi)

def merge_sort(a):
    aux = copy.deepcopy(a)
    _merge_sort_rec(a, aux, 0, len(a) - 1)
    return a

