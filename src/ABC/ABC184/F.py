import bisect
import itertools


def sum_list(lst):
    ret = {0}
    for i in range(1, len(lst) + 1):
        for sub_lst in itertools.combinations(lst, i):
            ret.add(sum(sub_lst))
    return list(ret)


n, t = map(int, input().split())
(*A,) = map(int, input().split())
X, Y = sum_list(A[: n // 2]), sum_list(A[n // 2 :])
Y.sort()
ans = 0
for x in X:
    if t < x:
        continue
    i = bisect.bisect_right(Y, t - x) - 1
    y = Y[i]
    ans = max(ans, x + y)
print(ans)
