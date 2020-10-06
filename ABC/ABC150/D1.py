def gcd(a, b):
    a_, b_ = a, b
    while a_:
        a_, b_ = b_ % a_, a_
    return b_


def lcm(a, b):
    return a * b // gcd(a, b)


def count(x):
    x_ = x
    cnt = 0
    while x_ % 2 == 0:
        x_ = x_ // 2
        cnt += 1
    return cnt


N, M = map(int, input().split())
(*A,) = map(int, input().split())
if len(set([count(a) for a in A])) > 1:
    print(0)
else:
    A = [a // 2 for a in A]
    while len(A) > 1:
        a = A.pop()
        b = A.pop()
        A.append(lcm(a, b))
    t = A.pop()
    q = M // t
    if q % 2 == 0:
        print(q // 2)
    else:
        print((q + 1) // 2)
