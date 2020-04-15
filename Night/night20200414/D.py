n = int(input())
*A, = map(int, input().split())
p = 10**9+7
s = 0
for i in range(n-1):
    for j in range(i+1, n):
        print(A[i], A[j], A[i] ^ A[j])
        s += A[i] ^ A[j]
        s %= p
print(s)
