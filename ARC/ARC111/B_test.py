n = int(input())
card = [tuple(map(int, input().split())) for _ in range(n)]
max_score = 0
for s in range(1 << n):
    bag = set()
    for i in range(n):
        x, y = card[i]
        if (1 << i) & s:
            bag.add(x)
        else:
            bag.add(y)
    max_score = max(max_score, len(bag))
print(max_score)
