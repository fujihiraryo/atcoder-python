import time
X, Y = 100000, 100
start = time.time()
A = [i + j for i in range(X) for j in range(Y)]
stop = time.time()
print(round(stop-start, 5))
start = time.time()
A = [i + j for i in range(Y) for j in range(X)]
stop = time.time()
print(round(stop-start, 5))
