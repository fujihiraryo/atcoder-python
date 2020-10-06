h, w, k = map(int, input().split())
C = [input() for i in range(h)]
ans = 0
for i in range(2 ** h):
    for j in range(2 ** w):
        cnt = 0
        for ii in range(h):
            for jj in range(w):
                if (i >> ii) & 1 == 0 and (j >> jj) & 1 == 0 and C[ii][jj] == "#":
                    cnt += 1
        if cnt == k:
            ans += 1
print(ans)
