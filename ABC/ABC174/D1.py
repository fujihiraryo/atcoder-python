n = int(input())
c = input()
ans = 0
l, r = 0, n - 1
while r - l > 0:
    if c[l] == "W" and c[r] == "R":
        ans += 1
        l += 1
        r -= 1
    if c[l] == "R":
        l += 1
    if c[r] == "W":
        r -= 1
print(ans)
