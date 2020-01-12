'''
凸関数fの最小値を3分探索で求める
'''


def f(x):
    return x + 1 / x


left = 0.1
right = 2
while right - left > 0.0001:
    if f(left) <= f(right):
        right = left + (right - left) * (2 / 3)
    else:
        left = left + (right - left) * (1 / 3)
print((left+right)/2, f((left+right)/2))
