x, n = map(int, input().split())
(*P,) = map(int, input().split())
Q = [q for q in range(1000) if q not in P]
dist = 1000
for q in Q:
    if abs(q - x) < dist:
        ans = q
        dist = abs(q - x)
print(ans)
