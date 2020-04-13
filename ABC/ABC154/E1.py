def DP(n, k):
    if k == 0:
        return 1
    elif n < 10 and k == 1:
        return n
    elif n < 10 and k != 0:
        return 0
    else:
        q, r = n//10, n % 10
        return DP(q, k)+r*DP(q, k-1)+(9-r)*DP(q-1, k-1)


n = int(input())
k = int(input())
print(DP(n, k))
