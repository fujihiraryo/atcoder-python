n = int(input())
(*A,) = map(int, input().split())
maxA = max(A)
# C[a] = A内のaの個数
C = {a: 0 for a in A}
for a in A:
    C[a] += 1
# D[a]=1: Aにaより小さいaの約数が存在する
D = {a: 0 for a in A}
for a in A:
    if C[a] > 0:
        t = 2
        while a * t <= maxA:
            D[a * t] = 1
            t += 1
ans = 0
for a in A:
    if C[a] == 1 and D[a] == 0:
        ans += 1
print(ans)
