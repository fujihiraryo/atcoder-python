n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]


def judge(x):
    s = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(n):
            s[i + 1][j + 1] = s[i][j + 1] + s[i + 1][j] - s[i][j]
            if a[i][j] <= x:
                s[i + 1][j + 1] += 1
    for i in range(k, n + 1):
        for j in range(k, n + 1):
            if s[i][j] - s[i - k][j] - s[i][j - k] + s[i - k][j - k] >= -(-k ** 2 // 2):
                return True
    return False


l, r = -1, 10 ** 9
while r - l > 1:
    x = (l + r) // 2
    if judge(x):
        r = x
    else:
        l = x
print(r)
