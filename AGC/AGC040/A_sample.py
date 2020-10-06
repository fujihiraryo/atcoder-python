N = 5 * (10 ** 5)
S = ["<" for n in range(N)]
S[1001] = ">"
S[2001] = ">"
print(*S)
