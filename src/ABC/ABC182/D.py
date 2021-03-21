n = int(input())
(*A,) = map(int, input().split())
S = [0] * n
S[0] = A[0]
for i in range(1, n):
    S[i] = S[i - 1] + A[i]
B = [0] * n
B[0] = S[0]
for i in range(1, n):
    B[i] = max(B[i - 1], S[i])
ans, last = 0, 0
for i in range(n):
    ans = max(ans, last + B[i])
    last += S[i]
print(ans)
