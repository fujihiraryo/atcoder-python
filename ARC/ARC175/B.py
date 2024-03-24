n, a, b = map(int, input().split())
a = min(a, 2 * b)
s = input()
s = [1 if s[i] == "(" else -1 for i in range(2 * n)]
cntL = s.count(1)
cntR = s.count(-1)
ans = 0
if cntL > cntR:
    for i in range(2 * n)[::-1]:
        if cntL == cntR:
            break
        if s[i] == 1:
            s[i] = -1
            cntL -= 1
            cntR += 1
            ans += b
if cntL < cntR:
    for i in range(2 * n):
        if cntL == cntR:
            break
        if s[i] == -1:
            s[i] = 1
            cntL += 1
            cntR -= 1
            ans += b
i = 0
j = 2 * n - 1
cntL = 0
cntR = 0
while i < j:
    si = s[i]
    sj = s[j]
    if s[i] == 1:
        if s[j] == -1:
            i += 1
            j -= 1
            cntL += 1
            cntR += 1
        else:  # s[j] == 1
            if cntR > 0:
                cntR -= 1
                j -= 1
            else:
                cntL += 1
                i += 1
    else:  # s[i] == -1
        if cntL > 0:
            cntL -= 1
            i += 1
        else:
            if s[j] == 1:
                if cntR > 0:
                    cntR -= 1
                    j -= 1
                else:
                    ans += a
                    s[i], s[j] = s[j], s[i]
                    # i += 1
                    # j -= 1
            else:
                cntR += 1
                j -= 1
print(ans)
