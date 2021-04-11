from fractions import Fraction


def score(hand):
    res = 0
    for i in range(1, 10):
        res += i * pow(10, hand[i])
    return res


k = int(input())
s = input()
t = input()
a = [0] * 10
for i in s[:-1]:
    a[int(i)] += 1
b = [0] * 10
for i in t[:-1]:
    b[int(i)] += 1
deck = [0] * 10
for i in range(1, 10):
    deck[i] = k - a[i] - b[i]
total = Fraction(0, 1)
for x in range(1, 10):
    for y in range(1, 10):
        a[x] += 1
        b[y] += 1
        if score(a) > score(b):
            p = Fraction(max(0, deck[x]), 9 * k - 8)
            deck[x] -= 1
            total += p * Fraction(max(0, deck[y]), 9 * k - 9)
            deck[x] += 1
        a[x] -= 1
        b[y] -= 1
print(float(total))
