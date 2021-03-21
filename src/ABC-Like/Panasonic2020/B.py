H, W = map(int, input().split())
ans = H * W
if H == 1 or W == 1:
    print(1)
    exit()
if ans % 2 == 0:
    print(ans // 2)
else:
    print((ans + 1) // 2)
