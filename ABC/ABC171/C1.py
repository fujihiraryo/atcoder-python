n = int(input())
ans = ""
while n:
    if n % 26 == 0:
        ans = "z" + ans
    else:
        ans = chr(ord("a") + n % 26 - 1) + ans
    n -= 1
    n //= 26
print(ans)
