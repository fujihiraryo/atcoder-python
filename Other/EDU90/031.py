import sys
from functools import lru_cache

sys.setrecursionlimit(10 ** 5)


@lru_cache(maxsize=None)
def grundy(i, j):
    s = set()
    if i > 0:
        s.add(grundy(i - 1, i + j))
    for k in range(1, j // 2 + 1):
        s.add(grundy(i, j - k))
    x = 0
    while x in s:
        x += 1
    return x


n = int(input())
*a, = map(int, input().split())
*b, = map(int, input().split())
ans = 0
for i, j in zip(a, b):
    ans ^= grundy(i, j)
print("First" if ans else "Second")
