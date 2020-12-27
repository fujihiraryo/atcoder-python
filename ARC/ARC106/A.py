n = int(input())
for a in range(1, 50):
    for b in range(1, 50):
        if 3 ** a + 5 ** b == n:
            print(a, b)
            exit()
print(-1)
