def ok(l):
    # 長さlの連続部分列で重ならずに2回以上現れるものがある
    D = {}
    for i in range(n-l+1):
        h = hash(S[i:i+l])
        try:
            if D[h] + l <= i:
                return True
        except:
            D[h] = i
    return False


S = 'abcdeaaaaaabcde'
n = len(S)
for l in range(1, n+1):
    print(ok(l))
