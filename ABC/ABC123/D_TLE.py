X, Y, Z, K = map(int, input().split())
*A, = sorted(map(int, input().split()), reverse=True)
*B, = sorted(map(int, input().split()), reverse=True)
*C, = sorted(map(int, input().split()), reverse=True)
AB = [A[x]+B[y] for x in range(X) for y in range(Y)]
AB.sort(reverse=True)
AB = AB[:K]
XY = len(AB)
ABC = [AB[xy]+C[z] for xy in range(XY) for z in range(Z)]
ABC.sort(reverse=True)
for k in range(K):
    print(ABC[k])
