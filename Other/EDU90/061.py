from collections import deque

d = deque()
for _ in range(int(input())):
    t, x = map(int, input().split())
    if t == 1:
        d.appendleft(x)
    elif t == 2:
        d.append(x)
    else:
        print(d[x - 1])
