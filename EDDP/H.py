h, w = map(int, input().split())
p = 10**9+7
S = []
for i in range(h):
    S.append(list(input()))
A = [[0 for j in range(w)] for i in range(h)]
flag = True
for i in range(h):
    if S[i][0] == '#':
        flag = False
    if flag:
        A[i][0] = 1
flag = True
for j in range(w):
    if S[0][j] == '#':
        flag = False
    if flag:
        A[0][j] = 1
for i in range(1, h):
    for j in range(1, w):
        if S[i][j] == '#':
            A[i][j] = 0
        else:
            A[i][j] = (A[i-1][j]+A[i][j-1]) % p
print(A[h-1][w-1])
