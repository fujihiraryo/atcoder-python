n, m, k = map(int, input().split())
(*A,) = map(int, input().split())
(*B,) = map(int, input().split())
SA, SB = [0], [0]
for i in range(n):
    SA.append(SA[i] + A[i])
for j in range(m):
    SB.append(SB[j] + B[j])
ans, tmp = 0, m
for i in range(n + 1):
    if SA[i] > k:
        break
    for j in range(tmp + 1)[::-1]:
        if SA[i] + SB[j] <= k:
            break
    ans = max(ans, i + j)
    tmp = j
print(ans)
