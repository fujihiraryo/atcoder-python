n, m = map(int, input().split())
(*A,) = map(int, input().split())
A.sort()
A = [0] + A + [n + 1]
k = 10 ** 20
B = []
for i in range(1, m + 2):
    b = A[i] - A[i - 1] - 1
    B.append(b)
    if b != 0:
        k = min(k, b)
ans = 0
for b in B:
    ans += -(-b // k)
print(ans)
