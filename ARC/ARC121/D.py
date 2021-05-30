n = int(input())
*a, = map(int, input().split())
ans = 10 ** 20
for x in range(n % 2, n, 2):
    b = a + [0] * x
    b.sort()
    m = len(b)
    c = [b[i] + b[m - 1 - i] for i in range(m // 2)]
    ans = min(ans, max(c) - min(c))
print(ans)
