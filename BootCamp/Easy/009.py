n = int(input())
k = int(input())
*X, = map(int, input().split())
s = 0
for x in X:
    s += min(x, k-x)
print(2*s)
