
def binary_search(input_array, value, pivot=0):
    _len = len(input_array)
    if _len == 1:
        if input_array[0] == value:
            return pivot
        else:
            return -1

    half = _len // 2
    val = input_array[half]
    if val == value:
        return half + pivot
    elif val < value:
        return binary_search(input_array[half:_len], value, pivot=pivot+half)
    else:
        return binary_search(input_array[0:half], value, pivot=pivot)
    return -1
