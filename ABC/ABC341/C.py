h, w, n = map(int, input().split())
t = input()
s = [input() for _ in range(h)]


def ok(i, j):
    if i < 0 or i >= h or j < 0 or j >= w:
        return False
    return s[i][j] == "."


def enable(i, j):
    if not ok(i, j):
        return False
    for k in range(n):
        if t[k] == "L":
            j -= 1
        elif t[k] == "R":
            j += 1
        elif t[k] == "U":
            i -= 1
        elif t[k] == "D":
            i += 1
        if not ok(i, j):
            return False
    return True


ans = 0
for i0 in range(h):
    for j0 in range(w):
        if enable(i0, j0):
            ans += 1
print(ans)
