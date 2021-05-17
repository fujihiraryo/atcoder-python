from math import gcd


def clockwise(a, b, p):
    ax, ay = a
    bx, by = b
    px, py = p
    return (bx - ax) * (py - ay) < (by - ay) * (px - ax)


def convex_hull(pl):
    pl.sort()
    n = len(pl)
    ul = []
    ul.append(pl[0])
    ul.append(pl[1])
    for i in range(2, n):
        while len(ul) >= 2 and not clockwise(ul[-2], ul[-1], pl[i]):
            ul.pop()
        ul.append(pl[i])
    ll = []
    ll.append(pl[-1])
    ll.append(pl[-2])
    for i in range(n - 2)[::-1]:
        while len(ll) >= 2 and not clockwise(ll[-2], ll[-1], pl[i]):
            ll.pop()
        ll.append(pl[i])
    return ul + ll[1:-1]


n = int(input())
lst = [tuple(map(int, input().split())) for _ in range(n)]
hull = convex_hull(lst)
m = len(hull)
area, bound = 0, 0
for i in range(m):
    x0, y0 = hull[i - 1]
    x1, y1 = hull[i]
    area += (x0 - x1) * (y0 + y1)
    bound += gcd(abs(x0 - x1), abs(y0 - y1))
ans = (bound + abs(area)) // 2 + 1 - n
print(ans)
