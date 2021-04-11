from itertools import permutations

s = [input() for _ in range(3)]
cnt = -1
dic = {}
for i in range(3):
    array = []
    for c in s[i]:
        if c not in dic:
            cnt += 1
            dic[c] = cnt
        array.append(dic[c])
    s[i] = array
if cnt >= 10:
    print("UNSOLVABLE")
    exit()
for p in permutations(range(10)):
    if any(p[s[i][0]] == 0 for i in range(3)):
        continue
    n = []
    for i in range(3):
        ni = 0
        t = 0
        for j in s[i][::-1]:
            ni += p[j] * pow(10, t)
            t += 1
        n.append(ni)
    if n[0] + n[1] == n[2]:
        print(*n, sep="\n")
        exit()
print("UNSOLVABLE")
