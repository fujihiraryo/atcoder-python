# 貪欲の改良版
d = int(input())
dd = d * (d + 1) // 2
(*C,) = map(int, input().split())
S = [list(map(int, input().split())) for i in range(d)]

max_score = -(10 ** 10)
best_T = None
for next_day in range(26):
    # Tの構築
    T = []
    L = [-1 for j in range(26)]
    for i in range(d):
        # 各日のスコア増加を最大にするjを選ぶ
        max_daily_score = -(10 ** 10)
        best_j = None
        for j in range(26):
            memo = L[j]
            L[j] = i
            # next_day日後までjがなかったときのdaily_scoreを計算
            daily_score = S[i][j]
            for jj in range(26):
                daily_score -= C[jj] * (i + next_day - L[jj])
            if daily_score > max_daily_score:
                max_daily_score = daily_score
                best_j = j
            L[j] = memo
        L[best_j] = i
        T.append(best_j)
    # スコアの計算
    L = [-1 for j in range(26)]
    X = [0 for j in range(26)]
    score = 0
    for i in range(d):
        score += S[i][T[i]]
        X[T[i]] += (d - i) * (i - L[T[i]])
        L[T[i]] = i
    for j in range(26):
        score -= C[j] * (dd - X[j])
    if score > max_score:
        max_score = score
        best_T = T
for t in best_T:
    print(t + 1)
