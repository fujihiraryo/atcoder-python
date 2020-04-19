k, n = map(int, input().split())
*A, = map(int, input().split())
B = []
for i in range(1, n):
    B.append(A[i]-A[i-1])
B.append(k-sum(B))
print(k-max(B))
