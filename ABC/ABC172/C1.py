import bisect

n, m, k = map(int, input().split())
(*A,) = map(int, input().split())
(*B,) = map(int, input().split())
SA, SB = [0], [0]
for i in range(n):
    SA.append(SA[i] + A[i])
for j in range(m):
    SB.append(SB[j] + B[j])
ans = 0
for i in range(n + 1):
    if SA[i] <= k:
        j = bisect.bisect_right(SB, k - SA[i]) - 1
        ans = max(ans, i + j)
print(ans)
