H, W, K = map(int, input().split())


def berry(char):
    if char == '#':
        return 1
    else:
        return 0


cake = [[berry(char) for char in input()] for h in range(H)]
ans_list = []

count = 0
for h in range(H):
    ans = []
    line = cake[h]
    if sum(line) == 0:
        ans_list.append(ans)
        continue
    count += 1
    flag = 1
    for w in range(W):
        block = line[w]
        if block == 1 and flag == 0:
            count += 1
        if block == 1:
            flag = 0
        ans.append(count)
    ans_list.append(ans)

for h in range(H):
    ans = ans_list[h]
    if ans == [] and h != H - 1:
        flag = 0
        for j in range(h + 1, H):
            if ans_list[j] != [] and flag == 0:
                ans_list[h] = ans_list[j]
            flag = 1
        for j in reversed(range(h + 1, H)):
            if ans_list[j] != [] and flag == 0:
                ans_list[h] = ans_list[j]
            flag = 1
    if ans == [] and h == H - 1:
        flag = 0
        for j in reversed(range(H)):
            if ans_list[j] != [] and flag == 0:
                ans_list[h] = ans_list[j]
            flag = 1
    print(*ans_list[h])
