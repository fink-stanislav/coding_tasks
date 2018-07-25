class CountingDict:

    def __init__(self):
        self.values = {}

    def add(self, value):
        try:
            self.values[value] += 1
        except KeyError:
            self.values[value] = 1

    def pop(self, value):
        try:
            result = self.values[value]
            if result == 0:
                return False
            else:
                self.values[value] -= 1
                return True
        except KeyError:
            return False

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    cd = CountingDict()
    for word in magazine:
        cd.add(word)

    for word in note:
        if not cd.pop(word):
            return False
    
    return True


class DictOfLists:
    def __init__(self):
        self.values = {}

    def add(self, key, value):
        try:
            self.values[key].append(value)
        except KeyError:
            self.values[key] = [value]

    def pop(self, key):
        try:
            value = self.values[key]
            value = sorted(value)
            result = value.pop()
            self.values[key] = value
            return result
        except KeyError:
            return False
