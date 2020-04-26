n, k = map(int, input().split())
*A, = map(int, input().split())
DP = [False] * (k+1)
for i in range(k+1):
    for a in A:
        if i+a <= k and not DP[i]:
            DP[i+a] = True
if DP[k]:
    print('First')
else:
    print('Second')
