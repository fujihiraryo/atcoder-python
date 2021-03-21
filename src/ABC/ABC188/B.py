n = int(input())
(*x,) = map(int, input().split())
(*y,) = map(int, input().split())
if sum(x[i] * y[i] for i in range(n)) == 0:
    print("Yes")
else:
    print("No")
