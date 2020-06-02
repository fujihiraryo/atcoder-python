# https://atcoder.jp/contests/abc085/tasks/abc085_c
n, y = map(int, input().split())
for a in range(n + 1):
    for b in range(n + 1):
        c = n - (a + b)
        if c >= 0 and 10000 * a + 5000 * b + 1000 * c == y:
            print(a, b, c)
            exit()
print(-1, -1, -1)
