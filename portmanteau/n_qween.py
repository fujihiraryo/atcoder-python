import itertools
import copy

C = [list(input()) for _ in range(8)]
rlst, clst = [], []
for i in range(8):
    rcnt, ccnt = 0, 0
    for j in range(8):
        if C[i][j] == 'Q':
            rcnt += 1
        if C[j][i] == 'Q':
            ccnt += 1
    if rcnt > 1 or ccnt > 1:
        print('No Answer')
        exit()
    if rcnt == 0:
        rlst.append(i)
    if ccnt == 0:
        clst.append(i)


def naname(i0, j0, i, j):
    return (i, j) != (i0, j0) and CC[i][j] == 'Q' and CC[i0][j0] == 'Q' and (i+j == i0+j0 or i-j == i0-j0)


def ok(CC):
    for i in range(8):
        for j in range(8):
            for i0 in range(8):
                for j0 in range(8):
                    if naname(i0, j0, i, j):
                        return False
    return True


for ctpl in itertools.permutations(clst):
    CC = copy.deepcopy(C)
    for k in range(5):
        CC[rlst[k]][ctpl[k]] = 'Q'
    if ok(CC):
        for r in CC:
            print(''.join(r))
        exit()
print('No Answer')
