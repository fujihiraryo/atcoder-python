n = int(input())
A = [int(input()) for i in range(n)]

l = 0
L = [l]
for a in A:
    l = max(l, a)
    L.append(l)

r = 0
R = [r]
for a in A[::-1]:
    r = max(r, a)
    R.append(r)
R.reverse()

for i in range(n):
    print(max(L[i], R[i + 1]))
