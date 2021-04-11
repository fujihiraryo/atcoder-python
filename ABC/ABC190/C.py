n, m = map(int, input().split())
a, b = [], []
for _ in range(m):
    ai, bi = map(int, input().split())
    a.append(ai - 1)
    b.append(bi - 1)
k = int(input())
c, d = [], []
for _ in range(k):
    ci, di = map(int, input().split())
    c.append(ci - 1)
    d.append(di - 1)


def count(state):
    cnt = 0
    for i in range(m):
        if state[a[i]] and state[b[i]]:
            cnt += 1
    return cnt


ans = 0
for s in range(1 << k):
    state = [0] * n
    for i in range(k):
        if (1 << i) & s:
            state[c[i]] = 1
        else:
            state[d[i]] = 1
    ans = max(ans, count(state))
print(ans)
