import itertools

N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))
A = list(itertools.permutations(range(1, N + 1)))
L = len(A)
X = []
for l in range(L):
    if A[l] == P or A[l] == Q:
        X.append(l)
print(max(X) - min(X))
