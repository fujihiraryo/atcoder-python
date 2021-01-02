from collections import defaultdict
from itertools import permutations


def factorize(x):
    factor = defaultdict(int)
    tmp = x
    i = 2
    while i ** 2 <= tmp:
        cnt = 0
        while tmp % i == 0:
            cnt += 1
            tmp //= i
        if cnt > 0:
            factor[i] = cnt
        i += 1
    if tmp != 1 or factor == {}:
        factor[tmp] = 1
    return factor


n = int(input())
total = defaultdict(int)
for i in range(2, n + 1):
    factor = factorize(i)
    for key in factor:
        total[key] += factor[key]
# (4,4,2)型
cnt = 0
for triple in permutations(total.keys(), 3):
    x, y, z = triple
    if total[x] >= 4 and total[y] >= 4 and total[z] >= 2:
        cnt += 1
cnt //= 2
# (14,4)型
for pair in permutations(total.keys(), 2):
    x, y = pair
    if total[x] >= 14 and total[y] >= 4:
        cnt += 1
# (24,2)型
for pair in permutations(total.keys(), 2):
    x, y = pair
    if total[x] >= 24 and total[y] >= 2:
        cnt += 1
# (74)型
for key in total.keys():
    if total[key] >= 74:
        cnt += 1
print(cnt)
