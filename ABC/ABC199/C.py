n = int(input())
s = list(input())
s = [s[:n], s[n:]]
for _ in range(int(input())):
    t, a, b = map(int, input().split())
    if t == 1:
        ia, ja = (a - 1) // n, (a - 1) % n
        ib, jb = (b - 1) // n, (b - 1) % n
        s[ia][ja], s[ib][jb] = s[ib][jb], s[ia][ja]
    else:
        s[0], s[1] = s[1], s[0]
print("".join(["".join(s[0]), "".join(s[1])]))
