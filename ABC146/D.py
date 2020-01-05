N=int(input())
G=[[] for n in range(N)]
E=[]
for n in range(N-1):
    a,b=map(int,input().split())
    E.append((a-1,b-1))
    G[a-1].append(b-1)
    G[b-1].append(a-1)
deg=[len(v) for v in G]
K=max(deg)
Q=G[0]
v0=0
X=[v0]
C=[0]*N
color={}
print(G)
while Q!=[]:
    v1=Q.pop(0)
    colors=list(range(1,K+1))
    if C[v0] in colors:
        colors.remove(C[v0])
    for child in G[v0]:
        if C[child] in colors:
            colors.remove(C[child])
    C[v1]=min(colors)
    color[(min(v0,v1),max(v0,v1))]=C[v1]
    X.append(v1)
    for w in G[v1]:
        if w not in X:
            Q.append(w)
    v0=v1
print(K)
print(color)
# for e in E:
#     print(color[e])