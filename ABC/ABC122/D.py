import itertools
import collections

MOD = 10 ** 9 + 7
n = int(input())
s = ("A", "C", "G", "T")
s = ["".join(x) for x in itertools.product(s, s, s)]
dp0 = collections.defaultdict(int)
for x in s:
    if x not in ("AGC", "GAC", "ACG"):
        dp0[x] = 1
for i in range(n - 3):
    dp1 = collections.defaultdict(int)
    for x in s:
        if x in ("AGC", "GAC", "ACG"):
            continue
        for y in s:
            if x == "AGA" and y == "GAC":
                continue
            if x == "AGG" and y == "GGC":
                continue
            if x == "AGT" and y == "GTC":
                continue
            if x == "ATG" and y == "TGC":
                continue
            if x[1:] == y[:2]:
                dp1[x] += dp0[y]
                dp1[x] %= MOD
    dp0 = dp1
print(sum(dp0[x] for x in s) % MOD)
