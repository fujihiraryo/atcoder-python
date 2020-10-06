import itertools

A = []
for i in range(8):
    C = list(input())
    try:
        A.append(C.index("Q"))
    except:
        A.append(-1)
if A.count(-1) != 5:
    print("No Answer")
    exit()
for X in itertools.permutations(range(8)):
    X = list(X)
    flag = True
    for i0, j0 in enumerate(X):
        for i1, j1 in enumerate(X):
            if i0 != i1 and (i0 + j0 == i1 + j1 or i0 - j0 == i1 - j1):
                flag = False
    if flag and all([X[i] == A[i] or A[i] == -1 for i in range(8)]):
        for x in X:
            S = list("........")
            S[x] = "Q"
            print("".join(S))
        exit()
print("No Answer")
