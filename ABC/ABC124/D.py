N, K = map(int, input().split())
S = input()
T = []
count = 1
for n in range(N - 1):
    s0, s1 = S[n], S[n + 1]
    if s0 == s1:
        count += 1
    else:
        T.append(count)
        count = 1
T.append(count)
if S[0] == '0':
    T = [0] + T
if S[-1] == '0':
    T = T + [0]
L = len(T)
if 2 * K + 1 >= L:
    print(N)
    exit()
# 偶数番目から始まる連続する2K+1個の和の最大値
now = sum(T[0: 2 * K + 1])
ans = now
for l in range(2, L - (2 * K + 1) + 1, 2):
    now -= T[l - 2]
    now -= T[l - 1]
    now += T[l + 2 * K - 1]
    now += T[l + 2 * K]
    if now > ans:
        ans = now
print(ans)
