def filter_duplicates(data):
    s = set()
    result = []
    for d in data:
        if d not in s:
            result.append(d)
        s.add(d)
    return result


l = [7, 6, 4, 3, 3, 4, 9]
print(filter_duplicates(l))
