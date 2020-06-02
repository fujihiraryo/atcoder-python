# ABC075/B
h, w = map(int, input().split())
S = [list(input()) for i in range(h)]
for i in range(h):
    for j in range(w):
        cnt = 0
        if S[i][j] == '.':
            for di in (-1, 0, 1):
                for dj in (-1, 0, 1):
                    if 0 <= i + di < h and 0 <= j + \
                            dj < w and S[i + di][j + dj] == '#':
                        cnt += 1
            S[i][j] = str(cnt)
    print(''.join(S[i]))
