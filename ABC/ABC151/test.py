n = 10
p = 10**9+7
F, I = [1], [1]
for i in range(1, n+1):
    F.append((F[-1]*i) % p)
    I.append((I[-1]*pow(i, p-2, p)) % p)
print(F)
print(I)
print((F[6]*I[2]*I[4]) % p)
