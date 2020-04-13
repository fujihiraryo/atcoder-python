import bisect
X = [None, None, 2, None]
i = bisect.bisect_left(X, 1)
print(i)
