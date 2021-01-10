n, m = map(int, input().split())
div = set()
i = 1
while i ** 2 <= m:
    if m % i == 0:
        div.add(i)
        div.add(m // i)
    i += 1
div = list(div)
div.sort(reverse=True)
for x in div:
    if m // x >= n:
        print(x)
        exit()
