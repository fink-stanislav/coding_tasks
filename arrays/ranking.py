
import math


def find_index0(arr, value):
    counter = 0
    for i in range(0, len(arr)):
        counter += 1
        if arr[i] <= value:
            print counter
            return i
    print counter
    return -1

def find_index1(arr, value, pred):
    counter = 0
    for i in range(0, pred):
        counter += 1
        if arr[i] <= value:
            print counter
            return i
    print counter
    return -1

def climbingLeaderboard0(scores, alice):
    #
    # Write your code here.
    #
    scores = sorted(list(set(scores)), reverse=True)
    _len = len(scores)
    ranks = []
    for a in alice:
        index = find_index0(scores, a)
        if index == -1:
            ranks.append(_len + 1)
        else:
            ranks.append(index + 1)

    return ranks

def climbingLeaderboard1(scores, alice):
    #
    # Write your code here.
    #
    scores = sorted(list(set(scores)), reverse=True)
    _len = len(scores)
    ranks = []
    index = _len
    for a in alice:
        index = find_index1(scores, a, index)
        if index == -1:
            ranks.append(_len + 1)
            index = _len
        else:
            ranks.append(index + 1)
            index = index + 1

    return ranks

def create_index(arr):
    _len = len(arr)
    number_of_indices = _len ** 0.5
    number_of_indices = int(math.floor(number_of_indices))

    rem = _len % number_of_indices
    amount = _len // number_of_indices

    index = []
    current_i = 0
    last_to = -1
    for _ in range(0, number_of_indices - 1):
        _from_i = current_i
        _to_i = _from_i + amount - 1
        if last_to > -1:
            _from = last_to - 1
        else:
            _from = arr[_from_i]
        _to = arr[_to_i]
        last_to = _to
        index.append([_from, _to, _from_i, _to_i])
        current_i = _to_i + 1

    _from_i = current_i
    _to_i = _from_i + amount + rem - 1
    _from = last_to - 1
    _to = arr[_to_i]
    index.append([_from, _to, _from_i, _to_i])

    return index

def get_index(index, a):
    result = None
    for v in index:
        _from = v[0]
        if a <= _from:
            result = v
    return result

def get_rank(index, scores, a):
    _from_i, _to_i = index[2], index[3]
    for i in range(_from_i, _to_i + 1):
        if a >= scores[i]:
            return i
    return -1

def climbingLeaderboard2(scores, alice):
    scores = sorted(list(set(scores)), reverse=True)
    index = create_index(scores)
    _len = len(scores)

    ranks = []
    for a in alice:
        i = get_index(index, a)
        if i is None:
            ranks.append(1)
        else:
            rank = get_rank(i, scores, a)
            if rank == -1:
                ranks.append(_len + 1)
            else:
                ranks.append(rank + 1)

    return ranks
