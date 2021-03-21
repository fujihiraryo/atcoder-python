N = int(input())
(*C,) = map(int, input().split())
C.sort(reverse=True)
p = 10 ** 9 + 7
S = 0
for i in range(N):
    S = (S + (i + 2) * C[i]) % p
S = (S * pow(4, N - 1, p)) % p
print(S)
