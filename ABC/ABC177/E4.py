n = int(input())
*A, = map(int, input().split())
m = max(A)
C = [0 for a in range(m + 1)]
for a in A:
    C[a] += 1
s = 0
for a in range(2, m + 1):
    s = max(s, sum(C[a::a]))
if s < 2:
    print('pairwise coprime')
elif s < n:
    print('setwise coprime')
else:
    print('not coprime')
