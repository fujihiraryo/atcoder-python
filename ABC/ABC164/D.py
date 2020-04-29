S = [int(i) for i in list(input())]
S.reverse()
T = [0]
for i in range(len(S)):
    T.append((T[-1] + S[i] * (pow(10, i, 2019))) % 2019)
C = {}
for t in T:
    try:
        C[t] += 1
    except BaseException:
        C[t] = 1
ans = 0
for c in C.values():
    ans += c * (c - 1) // 2
print(ans)
