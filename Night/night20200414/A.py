n, l = map(int, input().split())
z = 10**8
j = 0
s = 0
for i in range(n):
    s += l+i
    if abs(l+i) < z:
        z = abs(l+i)
        j = i
print(s-(l+j))
