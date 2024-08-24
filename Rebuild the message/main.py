def rebuild_message(parts):
    parts.sort(key=lambda s: s[0].lower())
    result = [parts[0]]
    for i in range(1, len(parts)):
        result.append(parts[i][1:])
    return ''.join(result)


parts = ["A---b", "b---Z"]
print(rebuild_message(parts))
parts = ["b---c", "c---Z", "A---b"]
print(rebuild_message(parts))
