b, c = map(int, input().split())
a0 = -b - (c - 1) // 2
a1 = -b + (c - 1) // 2
a2 = b - c // 2
a3 = b + max(0, c - 2) // 2
ans = abs(a0 - a1) + 1 + abs(a2 - a3) + 1
x, y = max(a0, a2), min(a1, a3)
if x <= y:
    ans -= abs(x - y) + 1
print(ans)
