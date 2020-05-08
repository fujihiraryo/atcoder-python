import bisect
n = int(input())
*A, = map(int, input().split())
B = [A[i] + i for i in range(n)]
C = [i - A[i] for i in range(n)]
B.sort()
C.sort()
ans = 0
for b in B:
    ans += bisect.bisect_right(C, b) - bisect.bisect_left(C, b)
print(ans)
