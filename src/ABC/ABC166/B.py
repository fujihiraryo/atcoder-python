n, k = map(int, input().split())
X = [True for i in range(n)]
for j in range(k):
    input()
    (*A,) = map(int, input().split())
    for a in A:
        X[a - 1] = False
print(len([x for x in X if x]))
