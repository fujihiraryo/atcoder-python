from itertools import combinations

n = int(input())
lstlst = [list(map(int, input().split())) for _ in range(n)]


def check(x):
    lst = []
    for i in range(n):
        tmp = 0
        for j in range(5):
            if lstlst[i][j] >= x:
                tmp += 1 << j
        lst.append(tmp)
    lst = lst[:3] + list(set(lst[3:]))
    for i, j, k in combinations(lst, 3):
        if (i | j | k) == (1 << 5) - 1:
            return True
    return False


a, b = 0, 10 ** 10
while b - a > 1:
    c = (a + b) // 2
    if check(c):
        a = c
    else:
        b = c
print(a)
