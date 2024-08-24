def compute_multiples_sum(n):
    total = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
            total += i
    return total


print(compute_multiples_sum(12))
