n, k = map(int, input().split())
lst = []
for _ in range(n):
    t, d = map(int, input().split())
    lst.append((d, t - 1))
lst.sort(reverse=True)
# 2枚以上あるカードの大きい方から2番目以降を手札とする
hand_all = [[] for _ in range(n)]
for d, t in lst[:k]:
    hand_all[t].append(d)
hand = []
for t in range(n):
    if len(hand_all[t]) < 2:
        continue
    hand_all[t].sort(reverse=True)
    for d in hand_all[t][1:]:
        hand.append(d)
hand.sort(reverse=True)
# 手札にない種類のカードを山札とする
stock_all = [[] for _ in range(n)]
for d, t in lst[k:]:
    stock_all[t].append(d)
stock = []
for t in range(n):
    if len(hand_all[t]) > 0 or len(stock_all[t]) == 0:
        continue
    stock.append(max(stock_all[t]))
stock.sort()
# 上位k個をとった場合の点数
x = sum(d for d, t in lst[:k])
y = len(set(t for d, t in lst[:k]))
ans = x + y ** 2
# 山札と手札を1枚ずつ交換していく
while hand and stock:
    x -= hand.pop()
    x += stock.pop()
    y += 1
    ans = max(ans, x + y ** 2)
print(ans)
