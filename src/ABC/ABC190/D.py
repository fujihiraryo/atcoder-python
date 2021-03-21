def div(x):
    s = {1, x}
    i = 1
    while i ** 2 < x:
        if x % i == 0:
            s.add(i)
            s.add(x // i)
        i += 1
    return s


n = int(input())
s = div(2 * n)
ans = 0
for x in s:
    if (2 * n // x - x + 1) % 2 == 0:
        ans += 1
print(ans)
