import time

n = 10 ** 8

start = time.time()
for i in range(n):
    for a in [1, 2, 3]:
        a + 1
stop = time.time()
print(stop - start)

start = time.time()
for i in range(n):
    for a in {1, 2, 3}:
        a + 1
stop = time.time()
print(stop - start)
