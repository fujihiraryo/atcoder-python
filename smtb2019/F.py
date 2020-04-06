t0, t1 = map(int, input().split())
a0, a1 = map(int, input().split())
b0, b1 = map(int, input().split())
d0 = (a0 - b0) * t0
d1 = (a1 - b1) * t1
if d0 < 0:
    d0, d1 = -d0, -d1
if d0 + d1 == 0:
    print('infinity')
    exit()
if d0 + d1 > 0:
    print(0)
    exit()
d = -(d0 + d1)
q, r = d0 // d, d0 % d
print(2 * q + min(r, 1))
