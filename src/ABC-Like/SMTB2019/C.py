X = int(input())
A = X // 100 * 100
B = A * 1.05
if A <= X <= B:
    print(1)
else:
    print(0)
