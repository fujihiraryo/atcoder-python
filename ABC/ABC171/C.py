n = int(input())
c = 1
tmp = 26
while tmp < n:
    tmp += 26 ** (c + 1)
    c += 1
ans = ""
for i in range(c):
    a = n % 26
    if a == 0:
        a = 26
    ans = chr(a + 96) + ans
    n = (n - a) // 26
print(ans)
