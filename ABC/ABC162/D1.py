n = int(input())
S = list(input())
R, G, B = set(), set(), set()
for i in range(n):
    if S[i] == "R":
        R.add(i)
    if S[i] == "G":
        G.add(i)
    if S[i] == "B":
        B.add(i)
cnt = len(R) * len(G) * len(B)
for r in R:
    for g in G:
        if 2 * g - r in B:
            cnt -= 1
        if 2 * r - g in B:
            cnt -= 1
        if (r + g) % 2 == 0 and (r + g) // 2 in B:
            cnt -= 1
print(cnt)
