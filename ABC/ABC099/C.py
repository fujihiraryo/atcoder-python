n = int(input())
F = [0]
for i in range(1, n + 1):
    A = [F[i - 1] + 1]
    j = 1
    while i - 6 ** j >= 0:
        A.append(F[i - 6 ** j] + 1)
        j += 1
    j = 1
    while i - 9 ** j >= 0:
        A.append(F[i - 9 ** j] + 1)
        j += 1
    F.append(min(A))
print(F[n])
