x, y = map(int, input().split())
for a in range(x + 1):
    if 2 * a + 4 * (x - a) == y:
        print("Yes")
        exit()
print("No")
