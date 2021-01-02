n = int(input())
ab = []
for _ in range(n):
    a, b = map(int, input().split())
    ab.append((a, b))
ab.sort(key=lambda x: -(2 * x[0] + x[1]))
sa = [0]
ss = [0]
for i in range(n):
    sa.append(sa[-1] + ab[i][0])
    ss.append(ss[-1] + ab[i][0] + ab[i][1])
for i in range(1, n + 1):
    if ss[i] > sa[n] - sa[i]:
        break
print(i)
