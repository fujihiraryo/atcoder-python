# bisectライブラリの使い方
import bisect
import time
import numpy as np
N = 10000000
A = [0] * N + [1] * N

start = time.time()
x = bisect.bisect_left(A, 1)
stop = time.time()
print(stop-start)

start = time.time()
A = np.array(A)
x = np.searchsorted(A, 1, side='left')
stop = time.time()
print(stop-start)
