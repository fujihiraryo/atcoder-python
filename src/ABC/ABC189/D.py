n = int(input())
x, y = 1, 1
for _ in range(n):
    s = input()
    if s == "AND":
        x, y = 2 * x + y, y
    else:
        x, y = x, x + 2 * y
print(y)
