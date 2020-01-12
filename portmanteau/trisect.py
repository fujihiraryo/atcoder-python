'''
凸関数fの最小値を3分探索で求める
'''


def f(x):
    return x + 1 / x


left = 0.1
right = 2
while right - left > 0.0001:
    left_ = left + (right - left) * (1 / 3)
    right_ = left + (right - left) * (2 / 3)
    if f(left_) <= f(right_):
        right = right_
    else:
        left = left_
x = (left + right) / 2
print(x, f(x))
