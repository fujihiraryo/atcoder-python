N, K = map(int, input().split())
(*H,) = map(int, input().split())
H.sort()
H.reverse()
for k in range(min(K, N)):
    H[k] = 0
print(sum(H))
