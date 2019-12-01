N = int(input())
S = input()
L = [str(i).zfill(3) for i in range(1000)]
count = 0
for l in L:
    try:
        i = S.index(l[0])
        j = S.index(l[1], i + 1)
        k = S.index(l[2], j + 1)
        count += 1
    except:
        continue
print(count)
