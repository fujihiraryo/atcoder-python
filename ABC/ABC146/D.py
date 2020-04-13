N=int(input())
G=[[] for n in range(N)]
E=[]
for n in range(N-1):
    a,b=map(int,input().split())
    E.append((a-1,b-1))
    G[a-1].append(b-1)
    G[b-1].append(a-1)
K=max([len(v) for v in G])

P=[-1]*N
Q=[0]
X=[]
count=0
while Q:
    v=Q.pop()
    X.append(v)
    for u in G[v]:
        if u==P[v]:
            continue
        P[u]=v
        Q.append(u)

C={}
for v in X:
    color=0
    try:
        p_color=C[min(v,P[v]),max(v,P[v])]
    except:
        p_color=-1
    for u in G[v]:
        if u==P[v]:
            continue
        if color==p_color:
            color+=1
        C[min(u,v),max(u,v)]=color
        color+=1

print(K)
for e in E:
    print(C[e]+1)
