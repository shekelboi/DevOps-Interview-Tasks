with open('input.txt') as file:
    total = 0
    for line in file:
        digits = [int(c) for c in line if c.isdigit()]
        if digits:
            total += max(digits)
    print(total)
