N, K, M = map(int, input().split())
A = list(map(int, input().split()))
a = sum(A)
t = N * M
if t - a <= K:
    print(str(max(t - a, 0)))
else:
    print(str(-1))
