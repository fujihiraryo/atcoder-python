import itertools
import time


def ok(x):
    # 配列が8queenの条件を満たすか
    for i0, j0 in enumerate(x):
        for i1, j1 in enumerate(x):
            if i0 != i1 and (i0 + j0 == i1 + j1 or i0 - j0 == i1 - j1):
                return False
    return True


start = time.time()
for n in range(1, 10 + 1):
    cnt = 0
    for x in itertools.permutations(range(n)):
        if ok(x):
            cnt += 1
    t = round(time.time() - start, 2)
    print(n, cnt, t)
