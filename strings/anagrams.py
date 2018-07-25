
def count(a, b):
    
    s1 = set(a) ^ set(b)

    return len(s1)