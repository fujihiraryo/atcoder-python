d = {"a": 0, "b": 1, "c": 2}
cards = [[d[x] for x in input()][::-1] for _ in range(3)]
turn = 0
while cards[turn]:
    turn = cards[turn].pop()
print(["A", "B", "C"][turn])
