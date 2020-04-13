n, k = map(int, input().split())
*P, = map(int, input().split())
x = sum((P[i]+1)/2 for i in range(k))
m = x
for i in range(1, n-k+1):
    x = x-(P[i-1]+1)/2+(P[i-1+k]+1)/2
    m = max(m, x)
print(m)
