# ABC153

## 結果

16 分 35 秒で ABCD の 4 完。\
パフォーマンス 906 \
1067 → 1052 (-15)

## E - Crested Ibis vs Monster

個数制限なしのナップザック問題。

```
DP[n][h] = 最初のn個を使ってAの和がhのときの最小コスト
DP[n][h] = min(DP[n-1][h], DP[n+1][h-A[n-1]]+B[n-1])
答えはDP[N][H]
```

として解けるが、python だと TLE となる。
