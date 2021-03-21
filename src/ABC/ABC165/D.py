a, b, n = map(int, input().split())


def f(x):
    return (a * x) // b - a * (x // b)


if n < b:
    print(f(n))
else:
    print(f(b - 1))
