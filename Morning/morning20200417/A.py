n, l = map(int, input().split())
m = 10**10
j = 0
s = 0
for i in range(n):
    a = abs(l+i)
    s += l+i
    if a < m:
        m = a
        j = i
print(s-(l+j))
