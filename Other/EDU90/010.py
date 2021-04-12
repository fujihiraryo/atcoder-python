n = int(input())
c, p = [], []
for _ in range(n):
    ci, pi = map(int, input().split())
    c.append(ci)
    p.append(pi)
s0 = [0] * (n + 1)
s1 = [0] * (n + 1)
for i in range(n):
    s0[i + 1] = s0[i]
    s1[i + 1] = s1[i]
    if c[i] == 1:
        s0[i + 1] += p[i]
    else:
        s1[i + 1] += p[i]
q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    print(s0[r] - s0[l - 1], s1[r] - s1[l - 1])
