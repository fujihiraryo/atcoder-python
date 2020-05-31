n = int(input())
AB = [tuple(map(int, input().split())) for i in range(n)]
A = sorted([a for a, b in AB])
B = sorted([b for a, b in AB])
if n % 2 == 0:
    print((B[n // 2 - 1] + B[n // 2]) - (A[n // 2 - 1] + A[n // 2]) + 1)
else:
    print(B[n // 2] - A[n // 2] + 1)
