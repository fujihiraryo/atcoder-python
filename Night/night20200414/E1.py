def zalgo(S):
    # SとS[i:n]のlcpの長さを記録した配列を返す
    n = len(S)
    A = [0] * n
    j = 0
    for i in range(1, n):
        if i+A[i-j] < j+A[j]:
            A[i] = A[i-j]
        else:
            k = max(0, A[j]-i+j)
            while i+k < n and S[k] == S[i+k]:
                k += 1
            A[i] = k
            j = i
    A[0] = n
    return A


n = int(input())
S = input()
l = 0
for i in range(n):
    A = zalgo(S[i:])
    B = [min(j, a) for j, a in enumerate(A)]
    l = max(l, max(B))
print(l)
