data = '1 2 3 4 5 6 15 17 18 24 88'.split()

res = map(int, data)
res = filter(lambda x: not x%2, res)
res = list(map(lambda x: (x, x**2), res))

print(res)