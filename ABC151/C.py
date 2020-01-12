N, M = map(int, input().split())
P, S = [], []
AC = [0 for n in range(N)]
WA = [0 for n in range(N)]
for m in range(M):
    p, s = input().split()
    p = int(p) - 1
    if AC[p] == 0 and s == 'WA':
        WA[p] += 1
    if s == 'AC':
        AC[p] = 1
AC_count = sum(AC)
WA_count = 0
for n in range(N):
    if AC[n] == 1:
        WA_count += WA[n]
print(AC_count, WA_count)
