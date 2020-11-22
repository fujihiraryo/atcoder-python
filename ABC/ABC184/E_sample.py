import random

h, w = 2000, 2000
print(h, w)
for i in range(h):
    raw = ""
    for j in range(w):
        if i == 0 and j == 0:
            a = "S"
        elif i == h - 1 and j == w - 1:
            a = "G"
        else:
            a = random.choice(["a", "b", "c", "d", ".", "#"])
        raw += a
    print(raw)
