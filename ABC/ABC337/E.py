n = int(input())
m = 0
while n > 2**m:
    m += 1
print(m)
for i in range(m):
    lst = []
    for j in range(n):
        if (j >> i) & 1:
            lst.append(j)
    print(len(lst), *lst)
s = input()
x = 0
for i in range(m):
    if s[i] == "1":
        x += 1 << i
if x == 0:
    print(n)
else:
    print(x)
