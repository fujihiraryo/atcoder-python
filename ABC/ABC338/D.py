n, m = map(int, input().split())
(*x,) = map(int, input().split())
s = [0] * n
for k in range(m - 1):
    i = x[k] - 1
    j = x[k + 1] - 1
    if i > j:
        i, j = j, i
    d = min(j - i, (i - j) % n)
    if j - i == d:
        s[0] += d
        s[i] += n - d - d
        s[j] += -(n - d) + d
    else:
        s[0] += n - d
        s[i] += -(n - d) + d
        s[j] += (n - d) - d
for i in range(1, n):
    s[i] += s[i - 1]
print(min(s))
