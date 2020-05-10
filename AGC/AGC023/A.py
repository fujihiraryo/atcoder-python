n = int(input())
*A, = map(int, input().split())
S = [0]
for i in range(n):
    S.append(S[-1] + A[i])
C = {}
for s in S:
    try:
        C[s] += 1
    except BaseException:
        C[s] = 1
print(sum([v * (v - 1) // 2 for v in C.values()]))
