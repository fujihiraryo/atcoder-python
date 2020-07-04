import random
d = 365
print(d)
C = [random.choice(range(100)) for j in range(26)]
print(*C)
for i in range(d):
    S = [random.choice(range(20000)) for j in range(26)]
    print(*S)
