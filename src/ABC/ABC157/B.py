A = [list(map(int, input().split())) for _ in range(3)]
N = int(input())
B = [int(input()) for _ in range(N)]
X = [[0 for _ in range(3)] for _ in range(3)]
for n in range(N):
    for i in range(3):
        for j in range(3):
            if A[i][j] == B[n]:
                X[i][j] = 1
tate = any([all([X[i][j] for j in range(3)]) for i in range(3)])
yoko = any([all([X[i][j] for i in range(3)]) for j in range(3)])
nana = all([X[i][i] for i in range(3)]) or all([X[i][2 - i] for i in range(3)])
if tate or yoko or nana:
    print("Yes")
else:
    print("No")
