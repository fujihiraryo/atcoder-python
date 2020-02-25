N, K = map(int, input().split())
K = min(N, K)
*h, = map(int, input().split())
a = [abs(h[0] - h[k]) for k in range(K)]
for n in range(N - K):
    a = a[1:] + [min([a[k] + abs(h[n + k] - h[n + K]) for k in range(K)])]
print(a[K - 1])
