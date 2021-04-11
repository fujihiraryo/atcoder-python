from itertools import product

MOD = 10 ** 9 + 7
a = 1
for i, j in product(range(5000), range(5000)):
    a = (a * (i + j + 1)) % MOD
