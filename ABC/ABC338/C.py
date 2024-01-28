n = int(input())
(*q,) = map(int, input().split())
(*a,) = map(int, input().split())
(*b,) = map(int, input().split())


def ok(s):
    for x in range(s + 1):
        y = s - x
        if all(a[i] * x + b[i] * y <= q[i] for i in range(n)):
            return True
    return False


sl, sr = 0, 2 * 10**6 + 1
while sr - sl > 1:
    sm = (sl + sr) // 2
    if ok(sm):
        sl = sm
    else:
        sr = sm
print(sl)
