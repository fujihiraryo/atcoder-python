N = int(input())
S, T = [], []
for n in range(N):
    s, t = input().split()
    S.append(s)
    T.append(int(t))
X = input()
T_sum = sum(T)
now_sum = 0
for n in range(N):
    now_sum += T[n]
    if X == S[n]:
        print(T_sum - now_sum)
        break
