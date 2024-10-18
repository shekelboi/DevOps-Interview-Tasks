from collections import Counter


def getUniqueCharacter(s: str) -> int:
    d = Counter(s)
    for i, c in enumerate(s):
        if d[c] == 1:
            return i + 1
    return -1


s = 'statistics'
print(getUniqueCharacter(s))
