def DP(n):
    if n < 4:
        return 0
    if n < 9:
        return 1
    if n == 9:
        return 2
    q, r = n//10, n % 10
    if r < 4:
        return (r+1)*DP(q)+(7-r)*DP(q-1)+2*q
    if r < 9:
        return r*DP(q)+(8-r)*DP(q-1)+2*q+1
    if r == 9:
        return 8*DP(q)+2*(q+1)


a, b = map(int, input().split())
print(DP(b)-DP(a-1))
