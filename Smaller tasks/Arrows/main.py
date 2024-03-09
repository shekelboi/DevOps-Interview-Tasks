def min_arrows(arrows):
    d = {}
    for a in arrows:
        if a not in d:
            d[a] = 1
        else:
            d[a] += 1
    return len(arrows) - max(d.values())


example1 = '^vv<v'
example2 = 'v>>>vv'
example3 = '<<<'
print(min_arrows(example1))
print(min_arrows(example2))
print(min_arrows(example3))
