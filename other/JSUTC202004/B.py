n = int(input())
X = []
for i in range(n):
    x, c = input().split()
    if c == "R":
        c = 0
    else:
        c = 1
    X.append((int(x), c))
X.sort(key=lambda x: (x[1], x[0]))
for x, c in X:
    print(x)
