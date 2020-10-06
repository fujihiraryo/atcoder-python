(*X,) = map(int, input().split())
for i in (1, 2, 3, 4, 5):
    if i != X[i - 1]:
        print(i)
        exit()
