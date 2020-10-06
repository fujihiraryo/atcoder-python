S = input()
N = len(S)
if N % 2 == 0:
    T0 = S[: N // 2] + S[: N // 2][::-1]
    T1 = S[::-1][: N // 2] + S[::-1][: N // 2][::-1]
else:
    T0 = S[: N // 2] + S[N // 2] + S[: N // 2][::-1]
    T1 = S[::-1][: N // 2] + S[N // 2] + S[::-1][: N // 2][::-1]
count0 = 0
count1 = 0
for n in range(N):
    if S[n] != T0[n]:
        count0 += 1
    if S[n] != T1[n]:
        count1 += 1
print(min(count0, count1))
