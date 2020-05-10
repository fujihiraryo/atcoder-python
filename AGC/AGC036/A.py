s = int(input())
if s == 10**18:
    print(0, 0, 10**9, 0, 0, 10**9)
    exit()
t = 10**9
a, b = s // t + 1, t - s % t
print(0, 0, 1, t, a, b)
