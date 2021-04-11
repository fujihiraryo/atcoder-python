n = int(input())
A = [int(input()) for i in range(n)]
A_ = sorted(A, reverse=True)
a0, a1 = A_[0], A_[1]
for a in A:
    if a == a0:
        print(a1)
    else:
        print(a0)
