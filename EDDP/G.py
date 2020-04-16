n, m = map(int, input().split())
G = [[] for i in range(n)]
I = [0 for i in range(n)]
for j in range(m):
    x, y = map(int, input().split())
    G[x-1].append(y-1)
    I[y-1] += 1
# Q:出発点の候補
Q = [i for i in range(n) if I[i] == 0]
# L[i]=iを終点とする最長パスの長さ
L = [0 for i in range(n)]
while Q:
    i = Q.pop()
    while G[i]:
        j = G[i].pop()
        I[j] -= 1
        L[j] = max(L[j], L[i]+1)
        if I[j] == 0:
            Q.append(j)
print(max(L))
