b, c = map(int, input().split())
a = (c - 1) // 2
if b < -b or a - b < b - c // 2:
    ans = a + 1 + c // 2 + 1
else:
    ans = max(a - b, b) - min(-b, b - c // 2) + 1
print(ans)
