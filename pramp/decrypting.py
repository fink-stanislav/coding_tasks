
def undo(pred, curr, _from=ord('a'), _to=ord('z')):
    _sum = pred + curr

    norm = _sum - _from

    mult = norm // 26

    diff = 26 * mult

    undone = diff + curr

    undone = undone - pred

    if undone > _to:
        undone -= 26
    elif undone < _from:
        undone += 26

    return undone

def decrypt(word):
    if len(word) == 0:
        return ''

    codes = [ord(c) for c in word]
    
    if len(word) > 1:
        pred = codes[0]
        for i in range(1, len(codes)):
            codes[i] = undo(pred, codes[i])
            pred += codes[i]
    
    codes[0] -= 1

    decrypted = [chr(i) for i in codes]

    return ''.join(decrypted)
