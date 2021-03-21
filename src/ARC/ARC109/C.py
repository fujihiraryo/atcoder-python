def hand(s):
    return {"R": 0, "P": 1, "S": 2}[s]


def select(x, y):
    if (x - y) % 3 == 1:
        return x
    else:
        return y


n, k = map(int, input().split())
n *= 2
s = input()
(*S,) = map(hand, list(s * 2))
for i in range(k):
    T = [select(S[i], S[i + 1]) for i in range(0, n, 2)]
    S = T * 2
print(("R", "P", "S")[S[0]])
