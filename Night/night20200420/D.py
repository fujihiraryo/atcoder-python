n = int(input())
*A, = map(int, input().split())
*B, = map(int, input().split())
*C, = map(int, input().split())
# n = 6
# A = [3, 14, 159, 2, 6, 53]
# B = [58, 9, 79, 323, 84, 6]
# C = [2643, 383, 2, 79, 50, 288]
A.sort()
B.sort()
C.sort()
# X[i]=B[i]<C[j]なるjの個数
X = []
j = 0
for i in range(n):
    while j < n and B[i] >= C[j]:
        j += 1
    X.append(n-j)
# S[i]=sum(X[:i])
S = [0]
for i in range(n):
    S.append(S[-1]+X[i])
# A[i]<B[j]なるjに対してS[n]-S[j]をたす
j = 0
ans = 0
for i in range(n):
    while j < n and A[i] >= B[j]:
        j += 1
    ans += S[n]-S[j]
print(ans)
