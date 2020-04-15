n = int(input())
*A, = map(int, input().split())
p = 10**9+7
A = [format(a, '060b') for a in A]
s = 0
for i in range(60):
    Ai = [a[i] for a in A]
    c0 = Ai.count('0')
    c1 = n-c0
    c = c0*c1
    s = (s+c*(2**(59-i))) % p
print(s)
