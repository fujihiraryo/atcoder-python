n, k = map(int, input().split())
(*A,) = map(int, input().split())
p = 10 ** 9 + 7
A.sort()
ans = 1
if A[n - 1] <= 0 and k % 2 == 1:
    for i in range(k):
        ans *= A[n - 1 - i]
        ans %= p
    print(ans)
    exit()
i = 0
j = n - 1
if k % 2 == 1:
    ans *= A[j]
    ans %= p
    j -= 1
    k -= 1
for _ in range(k // 2):
    left = A[i] * A[i + 1]
    right = A[j] * A[j - 1]
    if left > right:
        ans *= left
        ans %= p
        i += 2
    else:
        ans *= right
        ans %= p
        j -= 2
print(ans)
