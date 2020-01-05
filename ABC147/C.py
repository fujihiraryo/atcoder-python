N=int(input())
A,X,Y=[],[],[]
for n in range(N):
    An=int(input())
    Xn,Yn=[],[]
    for a in range(An):
        x,y=map(int,input().split())
        Xn.append(x-1)
        Yn.append(y)
    A.append(An)
    X.append(Xn)
    Y.append(Yn)

max_count=0
for k in range(2**N):
    P=[int(_) for _ in bin(k)[2:].zfill(N)]
    ok=True
    for i in range(N):
        for j in range(A[i]):
            if P[i]==1 and P[X[i][j]]!=Y[i][j]:
                ok=False
    if ok:
        max_count=max(max_count,sum(P))
print(max_count)
