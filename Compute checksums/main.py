def compute_checksums(file_bytes):
    result = []
    index = 0
    while index < len(file_bytes):
        header = file_bytes[index]
        index += 1
        total = sum(file_bytes[index:index + header])
        result.append(total % 256)
        index += header
    return result


data = [3, 44, 55, 66, 2, 110, 220]
print(compute_checksums(data))
