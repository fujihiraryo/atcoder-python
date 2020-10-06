n = int(input())
(*A,) = map(int, input().split())
F = {}
for i, a in enumerate(A):
    try:
        F[a] += 1
    except:
        F[a] = 1
for i in range(1, n + 1):
    try:
        print(F[i])
    except:
        print(0)
