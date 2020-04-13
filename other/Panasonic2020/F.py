def tri(x):
    x0 = x
    y = []
    while x0 > 0:
        y.append(x0 % 3)
        x0 = x0 // 3
    return ([0] * 30 + y)[-30:]


def trans(a, b):
    return tri(a), tri(b)


Q = int(input())
