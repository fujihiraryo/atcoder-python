k, g, m = map(int, input().split())
glass = 0
mag = 0
for _ in range(k):
    if glass == g:
        glass = 0
    elif mag == 0:
        mag = m
    else:
        while mag > 0 and glass < g:
            mag -= 1
            glass += 1
print(glass, mag)
