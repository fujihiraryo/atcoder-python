h, w = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(h)]
B = [A[i][j] for i in range(h) for j in range(w)]
minB = min(B)
print(sum(B[i] - minB for i in range(h * w)))
