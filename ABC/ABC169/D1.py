n = int(input())
if n == 1:
    print(0)
    exit()
F = {}
tmp = n
i = 2
while i ** 2 <= tmp:
    cnt = 0
    while tmp % i == 0:
        cnt += 1
        tmp //= i
    if cnt > 0:
        F[i] = cnt
    i += 1
if tmp != 1 or F == {}:
    F[tmp] = 1
ans = 0
for p in F:
    a = 1
    while F[p] >= a:
        F[p] -= a
        ans += 1
        a += 1
print(ans)
