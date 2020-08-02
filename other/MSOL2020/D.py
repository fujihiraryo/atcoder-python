n = int(input())
*A, = map(int, input().split())
ans = 1000
for i in range(n - 1):
    ans += (ans // A[i]) * max(A[i + 1] - A[i], 0)
print(ans)
