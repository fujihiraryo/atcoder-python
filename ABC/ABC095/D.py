n, c = map(int, input().split())
XV = [tuple(map(int, input().split())) for i in range(n)]
X = [x for x, v in XV]
V = [v for x, v in XV]
S = [0]
for i in range(n):
    S.append(S[-1]+V[i])
# 右回りから行く場合
A = [0]
for i in range(1, n+1):
    A.append(max(A[-1], S[i]-2*X[i-1]))
B = []
for i in range(n):
    B.append(S[n]-S[i]-(c-X[i]))
B.append(0)
ans0 = max([A[i]+B[i] for i in range(n+1)])
# 左回りから行く場合
A = [0]
for i in range(1, n+1):
    A.append(max(A[-1], S[i]-X[i-1]))
B = []
for i in range(n):
    B.append(S[n]-S[i]-2*(c-X[i]))
B.append(0)
ans1 = max([A[i]+B[i] for i in range(n+1)])
print(max(ans0, ans1))
