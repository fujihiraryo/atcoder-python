import bisect
n = int(input())
*A, = map(int, input().split())
inf = 10**10
DP = [inf for i in range(n)]
for a in A:
    i = bisect.bisect_left(DP, a)
    DP[i] = a
print(bisect.bisect_left(DP, inf))
