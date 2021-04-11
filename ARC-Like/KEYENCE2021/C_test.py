from collections import defaultdict
from itertools import product

MOD = 10 ** 9 + 7
a = defaultdict(int)
a[(0, 0)] = 1
for i, j in product(range(5000), range(5000)):
    a[(i + 1, j)] += a[(i, j)]
    a[(i + 1, j)] %= MOD
    a[(i, j + 1)] += a[(i, j)]
    a[(i, j + 1)] %= MOD
for i in range(10):
    print(*[a[(i, j)] for j in range(10)])
