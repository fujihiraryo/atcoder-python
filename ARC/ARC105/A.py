lst = list(map(int, input().split()))
for bit in range(1 << 4):
    a, b = 0, 0
    for i in range(4):
        if (1 << i) & bit:
            a += lst[i]
        else:
            b += lst[i]
    if a == b:
        print("Yes")
        exit()
print("No")
