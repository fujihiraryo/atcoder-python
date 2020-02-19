N, K = map(int, input().split())
* P, = map(int, input().split())
P = [(1+p)/2 for p in P]
M1 = sum(P[:K])
M0 = M1
for i in range(K, N):
    M0 += P[i]
    M0 -= P[i - K]
    if M0 > M1:
        M1 = M0
print(M1)
