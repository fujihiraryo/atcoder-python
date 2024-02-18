import bisect


def lis(a):
    # a[:i]の最長増加部分列の長さ
    res = [0]
    b = []
    for x in a:
        i = bisect.bisect_left(b, x)
        if i == len(b):
            b.append(x)
        else:
            b[i] = x
        res.append(len(b))
    return res


n = int(input())
(*a,) = map(int, input().split())
b0 = lis(a)
b1 = lis(a[::-1])[::-1]
print(max(b0[i + 1] + b1[i] for i in range(n)) - 1)
