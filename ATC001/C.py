import numpy as np

N = int(input())
A, B = [0], [0]
for i in range(1, N+1):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

C = np.fft.irfft(np.fft.rfft(A, 2*(N+1)) * np.fft.rfft(B, 2*(N+1)))
for k in range(1, 2*N+1):
    print(int(round(C[k])))
