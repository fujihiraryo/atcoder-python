n, d, a = map(int, input().split())
XH = []
for i in range(n):
    x, h = map(int, input().split())
    XH.append((x, h))
XH.sort()
X = [x for x, h in XH]
H = [h for x, h in XH]
X.append(10**10)
H.append(0)
j = 0
c = 0
S = [0]*(n+1)
for i in range(n):
    H[i] = max(0, H[i]-S[i])
    c += -(-H[i]//a)
    while X[j] <= X[i] + 2*d:
        j += 1
    S[i+1] += S[i] + -(-H[i]//a)*a
    S[j] -= -(-H[i]//a)*a
print(c)
