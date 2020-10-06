N, M = map(int, input().split())
S, C = [], []
for m in range(M):
    s, c = map(int, input().split())
    S.append(s)
    C.append(c)
if N == 1:
    if all([c == 0 for c in C]):
        print(0)
        exit()
for n in range(10 ** (N - 1), 10 ** N):
    if all([int(str(n)[S[m] - 1]) == C[m] for m in range(M)]):
        print(n)
        exit()
print(-1)
