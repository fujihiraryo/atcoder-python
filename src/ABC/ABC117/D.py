n, k = map(int, input().split())
(*a,) = map(int, input().split())
x = 0
bit_k = bin(k)[2:]
for i in range(len(bit_k))[::-1]:
    if sum((1 << i) & a[j] > 0 for j in range(n)) * 2 <= n and x + (1 << i) <= k:
        x += 1 << i
print(sum(x ^ a[j] for j in range(n)))
