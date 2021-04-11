import collections

N = int(input())
S = [input() for n in range(N)]
S = collections.Counter(S)
M = S.most_common()[0][1]
S = sorted(S.items(), key=lambda _: _[0])
for s in S:
    if s[1] == M:
        print(s[0])
