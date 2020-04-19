A = [list(map(int, input().split())) for i in range(3)]
B = [[0]*3 for i in range(3)]
n = int(input())
for k in range(n):
    b = int(input())
    for i in range(3):
        for j in range(3):
            if A[i][j] == b:
                B[i][j] = 1
if any([all([B[i][j] == 1 for j in range(3)]) for i in range(3)]):
    print('Yes')
    exit()
if any([all([B[i][j] == 1 for i in range(3)]) for j in range(3)]):
    print('Yes')
    exit()
if B[0][0]*B[1][1]*B[2][2] == 1:
    print('Yes')
    exit()
if B[0][2]*B[1][1]*B[2][0] == 1:
    print('Yes')
    exit()
print('No')
