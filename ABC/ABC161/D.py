X = [1, 2, 3, 4, 5, 6, 7, 8, 9]
A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(9):
    B = []
    for a in A:
        r = a % 10
        if r > 0:
            B.append(10*a+r-1)
        if r < 9:
            B.append(10*a+r+1)
        B.append(10*a+r)
    X = X+B
    A = B
X.sort()
k = int(input())
print(X[k-1])
