N, P = map(int, input().split())
S = [int(_) for _ in list(input())]
if P == 2 or P == 5:
    ans = 0
    for n in range(N):
        if S[n] % P == 0:
            ans += n + 1
    print(ans)
else:
    S = [(S[n] * pow(10, N - n - 1, P)) % P for n in range(N)]
    S.reverse()
    T = [0]
    for s in S:
        T.append((T[-1] + s) % P)
    lst = {i: 0 for i in range(P)}
    ans = 0
    for t in T:
        ans += lst[t]
        lst[t] += 1
    print(ans)
