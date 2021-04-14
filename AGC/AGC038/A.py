h, w, b, a = map(int, input().split())
if h < 2 * a or w < 2 * b:
    print("No")
    exit()
ans = [["0"] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if i < a and j < b:
            ans[i][j] = "1"
        if i >= a and j >= b:
            ans[i][j] = "1"
for raw in ans:
    print("".join(raw))
