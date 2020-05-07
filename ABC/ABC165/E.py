n, m = map(int, input().split())


def dist(a, b):
    return min(abs(a - b), n - abs(a - b))


a, b = n, 1
S = set()
for i in range(m):
    if 2 * dist(a, b) == n or dist(a, b) in S:
        a -= 1
    print(a, b)
    S.add(dist(a, b))
    a -= 1
    b += 1
