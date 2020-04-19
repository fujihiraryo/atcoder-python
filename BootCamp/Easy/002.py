n = int(input())
*X, = map(int, input().split())
m = 10**10
for i in range(1, 100+1):
    m = min(m, sum([(x-i)**2 for x in X]))
print(m)
