import random

h, w = 1, 3
q = 100
print(h, w)
print(q)
for _ in range(q):
    t = random.choice((1, 2))
    if t == 1:
        r = random.randrange(1, h + 1)
        c = random.randrange(1, w + 1)
        print(t, r, c)
    else:
        ra = random.randrange(1, h + 1)
        ca = random.randrange(1, w + 1)
        rb = random.randrange(1, h + 1)
        cb = random.randrange(1, w + 1)
        print(t, ra, ca, rb, cb)
