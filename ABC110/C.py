def f(A):
    dct = {}
    B = []
    i = 0
    for a in A:
        try:
            dct[a]
        except:
            dct[a] = i
            i += 1
        B.append(dct[a])
    return B


S = f(list(input()))
T = f(list(input()))
if S == T:
    print('Yes')
else:
    print('No')
