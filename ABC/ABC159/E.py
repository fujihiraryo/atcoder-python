# 部分リストのリスト
def all_sublist(lst):
    lstlst = []
    for i in range(2 ** len(lst)):
        sublst = []
        for j in range(len(lst)):
            if (i >> j) & 1 == 1:
                sublst.append(lst[j])
        lstlst.append(sublst)
    return lstlst


# 入力
H, W, K = map(int, input().split())
S = [[int(x) for x in list(input())] for h in range(H)]

# 横方向にカットする位置の列挙
cutlst = all_sublist(list(range(1, H)))

# 横方向の切り方を動かして切る数の合計の最小値を求める
cnt_min = 10 ** 9 + 7
for cut in cutlst:
    # 横方向に切って圧縮したものをSSとする
    SS = []
    cut.append(H)
    start = 0
    for stop in cut:
        T = []
        for w in range(W):
            tmp = 0
            for h in range(start, stop):
                tmp += S[h][w]
            T.append(tmp)
        SS.append(T)
        start = stop
    H0 = len(SS)
    # K以上の成分があったらこのcutはパス
    if any([SS[h][w] > K for h in range(H0) for w in range(W)]):
        continue
    # 縦方向に切る数を数える
    cnt = len(cut) - 1
    left = [0 for h in range(H0)]
    right = [SS[h][0] for h in range(H0)]
    for w in range(1, W):
        left, right = right, [right[h] + SS[h][w] for h in range(H0)]
        leftOK = all([left[h] <= K for h in range(H0)])
        rightNG = any([right[h] > K for h in range(H0)])
        # すべての成分がK以下になるギリギリのところで切る
        if leftOK and rightNG:
            left = [0 for h in range(H0)]
            right = [SS[h][w] for h in range(H0)]
            cnt += 1
    cnt_min = min(cnt_min, cnt)
print(cnt_min)
