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


def merge_sort(arr):
    _len = len(arr)
    _arrays = []
    if _len % 2 != 0:
        _len -= 1
        _arrays = [[arr[0]]]
    arr = arr[1:]
    _arrays += [[arr[q-1], arr[q]] for q in range(1, _len, 2)]

    for w in _arrays:
        for x in range(1, len(w)):
            if w[x-1] > w[x]:
                swap(w, x - 1, x)

    while len(_arrays) > 1:
        new_arrays = []
        for i in range(1, len(_arrays), 2):
            a = copy.deepcopy(_arrays[i - 1])
            b = copy.deepcopy(_arrays[i])
            _len_a = len(a)
            _len_b = len(b)
            _len = max(_len_a, _len_b)
            new_array = []
            aj = None
            bj = None
            while _len_a + _len_b != len(new_array):
                if len(a) > 0 and aj is None:
                    aj = a.pop(0)
                if len(b) > 0 and bj is None:
                    bj = b.pop(0)

                if aj or bj:
                    if aj >= bj:
                        if bj is None:
                            new_array.append(aj)
                            aj = None
                        else:
                            new_array.append(bj)
                        bj = None

                if aj or bj:
                    if bj >= aj:
                        if aj is None:
                            new_array.append(bj)
                            bj = None
                        else:
                            new_array.append(aj)
                        aj = None
            new_arrays.append(new_array)
        _arrays = new_arrays
    return _arrays[0]

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
