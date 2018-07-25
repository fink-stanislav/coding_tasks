

def find_diffs(arr, element):
    diffs = []
    for i in range(0, len(arr)):
        diff = abs(arr[i] - element)
        diffs.append(diff)
    return diffs

def are_all_equal(arr):
    diffs = find_diffs(arr, arr[0])
    return sum(diffs) == 0

def max_count(arr):
    counts = {}
    for a in enumerate(arr):
        if a[1] in counts:
            counts[a[1]]['count'] += 1
        else:
            counts[a[1]] = {'index': a[0], 'count': 1}

    return counts

def index_and_value(arr):
    _value = min(arr)
    _index = arr.index(_value)

    diffs = find_diffs(arr, _value)

    diffs_count = max_count(diffs)
    biggest_diff = max(diffs_count.keys())
    most_different = diffs_count[biggest_diff]
    _index = most_different['index']

    """
    biggest_diff = [k for k in diffs_count.keys() if k > 0]
    biggest_diff = min(biggest_diff)
    most_different = diffs_count[biggest_diff]
    _index = most_different['index']
    """

    if biggest_diff == 1 or biggest_diff == 3 or biggest_diff == 5:
        _value = biggest_diff
    else:
        if biggest_diff == 2 or biggest_diff == 4:
            _value = 1
        else:
            if biggest_diff > 5:
                _value = 5

    return {'index': _index, 'value': _value}

def make_equal(arr):
    iv = index_and_value(arr)

    for i in range(0, len(arr)):
        if i != iv['index']:
            arr[i] += iv['value']

    return arr

def _equal(arr):
    counter = 0
    while not are_all_equal(arr):
        arr = make_equal(arr)
        counter += 1

    return counter
