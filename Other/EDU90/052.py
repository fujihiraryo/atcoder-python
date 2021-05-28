MOD = 10 ** 9 + 7
n = int(input())
ans = 1
for _ in range(n):
    *a, = map(int, input().split())
    ans *= sum(a)
    ans %= MOD
print(ans)
