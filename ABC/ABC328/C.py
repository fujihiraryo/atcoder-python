n, q = map(int, input().split())
s = input()
a = [0] * n
for i in range(n - 1):
    if s[i] == s[i + 1]:
        a[i] = 1
b = [0] * (n + 1)
for i in range(1, n + 1):
    b[i] = b[i - 1] + a[i - 1]
for _ in range(q):
    l, r = map(int, input().split())
    print(b[r - 1] - b[l - 1])
