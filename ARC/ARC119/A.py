ans = 10 ** 30
n = int(input())
for b in range(61):
    a, c = n // 2 ** b, n % 2 ** b
    ans = min(ans, a + b + c)
print(ans)
