N = int(input())
S, T = input().split()
X = ""
for n in range(N):
    X += S[n] + T[n]
print(X)
