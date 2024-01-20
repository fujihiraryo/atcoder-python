INF = 10**20
h, w, k = map(int, input().split())
s = [input() for _ in range(h)]


def ans(lst):
    cnt_o = 0
    cnt_x = 0
    for i in range(min(k, len(lst))):
        if lst[i] == "o":
            cnt_o += 1
        elif lst[i] == "x":
            cnt_x += 1
    if cnt_x == 0:
        res = max(0, k - cnt_o)
    else:
        res = INF
    for i in range(1, len(lst) - k + 1):
        if lst[i - 1] == "o":
            cnt_o -= 1
        elif lst[i - 1] == "x":
            cnt_x -= 1
        if lst[i + k - 1] == "o":
            cnt_o += 1
        elif lst[i + k - 1] == "x":
            cnt_x += 1
        if cnt_x == 0:
            res = min(res, k - cnt_o)
    return res


ans_row = min([ans(s[i]) for i in range(h)])
ans_col = min([ans([s[i][j] for i in range(h)]) for j in range(w)])
ans = min(ans_row, ans_col)
if ans < INF:
    print(ans)
else:
    print(-1)
