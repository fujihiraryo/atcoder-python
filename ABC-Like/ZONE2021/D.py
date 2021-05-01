from collections import deque

s = input()
t = deque()
sgn = 1
for c in s:
    if c == "R":
        sgn *= -1
    elif len(t) == 0:
        t.append(c)
    elif sgn == 1:
        x = t.pop()
        if c == x:
            continue
        else:
            t.append(x)
            t.append(c)
    elif sgn == -1:
        x = t.popleft()
        if c == x:
            continue
        else:
            t.appendleft(x)
            t.appendleft(c)
if sgn == -1:
    t.reverse()
print("".join(t))
