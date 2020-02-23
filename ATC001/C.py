import numpy as np

N = int(input())
A, B = [], []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

C = np.fft.irfft(np.fft.rfft(A, 2*10**5) * np.fft.rfft(B, 2*10**5))
print(0)
for i in range(2*N-1):
    print(int(round(C[i])))
