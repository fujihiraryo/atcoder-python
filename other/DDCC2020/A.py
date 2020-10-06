X, Y = map(int, input().split())
ans = 100000 * max(4 - X, 0) + 100000 * max(4 - Y, 0)
if X == 1 and Y == 1:
    ans += 400000
print(ans)
