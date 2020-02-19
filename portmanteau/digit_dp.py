# 0以上N以下の自然数のうち、3を使っている個数
def f(N):
    M, R = N // 10, N % 10
    if M == 0:
        if R < 3:
            return 0
        else:
            return 1
    else:
        if R < 3:
            return (R+1)*f(M)+(8-R)*f(M-1)+M
        else:
            return R*f(M)+(M+1)+(9-R)*f(M+1)


def g(N):
    cnt = 0
    for n in range(N+1):
        if '3' in str(n):
            cnt += 1
    return cnt


print(f(40), g(40))
