N = int(input())
A = []
for n in range(N):
    A.append(int(input()))
B = [0 for n in range(N)]
B[0] = A[0]
for n in range(N - 1):
    B[n + 1] = max(B[n], A[n + 1])
C = [0 for n in range(N)]
C[-1] = A[-1]
for n in range(N - 1):
    C[-n - 2] = max(C[-n - 1], A[-n - 2])
for n in range(N):
    if n == 0:
        print(C[1])
    elif n == N - 1:
        print(B[N - 2])
    else:
        print(max(B[n - 1], C[n + 1]))
