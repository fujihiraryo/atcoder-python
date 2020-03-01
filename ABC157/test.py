def div2(n):
    # n<=2**xをみたす最小のxを求める
    tmp = n
    cnt = 0
    while (tmp + 1) // 2 > 0:
        tmp //= 2
        cnt += 1
    return cnt


print(div2(2))