n = int(input())
ans = 0
i = 0
while n >= pow(10, 3 * (i + 1)):
    ans += (pow(10, 3 * (i + 1)) - pow(10, 3 * i)) * i
    i += 1
ans += (n - pow(10, 3 * i) + 1) * i
print(ans)
