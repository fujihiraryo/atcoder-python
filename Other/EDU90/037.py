from collections import deque

INF = 1 << 60
w, n = map(int, input().split())
l, r, v = [], [], []
for _ in range(n):
    li, ri, vi = map(int, input().split())
    l.append(li)
    r.append(ri)
    v.append(vi)
lst = [-INF] * (w + 1)
lst[0] = 0
for i in range(n):
    new = lst[:]
    dq = deque()
    for j in range(l[i], w + 1):
        while dq and lst[dq[-1]] <= lst[j - l[i]]:
            dq.pop()
        dq.append(j - l[i])
        while dq and dq[0] < j - r[i]:
            dq.popleft()
        new[j] = max(new[j], lst[dq[0]] + v[i])
    lst = new
ans = lst[w]
print(ans if ans > 0 else -1)
