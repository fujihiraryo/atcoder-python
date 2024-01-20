n = int(input())
sx, sy = 0, 0
for i in range(n):
    x, y = map(int, input().split())
    sx += x
    sy += y
if sx > sy:
    print("Takahashi")
if sx == sy:
    print("Draw")
if sx < sy:
    print("Aoki")
