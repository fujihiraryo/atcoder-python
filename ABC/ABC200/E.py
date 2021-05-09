def cmb(a, b):
    if a < b:
        return 0
    if b == 1:
        return a
    elif b == 2:
        return a * (a - 1) // 2


def f(x):
    # 和がxになる3つの数の組の個数
    global n
    return (
        cmb(x + 2, 2)
        - 3 * cmb(x - n + 2, 2)
        + 3 * cmb(x - 2 * n + 2, 2)
        - cmb(x - 3 * n + 2, 2)
    )


def g(x):
    # 和がxになる2つの数の組の個数
    global n
    return cmb(x + 1, 1) - 2 * cmb(x - n + 1, 1) + cmb(x - 2 * n + 1, 1)


def h(x, j):
    # 和がxの3つの数の組を昇順に並べたときのk番目
    global n
    t = 0
    for a in range(n):
        if j < t + g(x - a):
            break
        t += g(x - a)
    b = max(0, x - a - n + 1) + j - t
    c = x - a - b
    return a, b, c


n, k = map(int, input().split())
k -= 1
t = 0
for x in range(3 * n):
    if k < t + f(x):
        break
    t += f(x)
a, b, c = h(x, k - t)
print(a + 1, b + 1, c + 1)
