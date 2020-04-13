h, w, k = map(int, input().split())
S = [list(input()) for i in range(h)]
A = []
cnt = 1
for i in range(h):
    Ai = []
    if S[i].count('#') == 0:
        A.append(Ai)
        continue
    flag = False
    for j in range(w):
        if S[i][j] == '#':
            if flag:
                cnt += 1
            flag = True
        Ai.append(cnt)
    A.append(Ai)
    cnt += 1

l = 0
for i in range(h):
    if A[i] != []:
        for j in range(l, i):
            A[j] = A[i]
        l = i + 1
for j in range(l, h):
    A[j] = A[l - 1]

for i in range(h):
    print(*A[i])
