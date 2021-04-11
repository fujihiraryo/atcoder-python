n = int(input())
XY = [tuple(map(int, input().split())) for i in range(n)]
A = [x + y for x, y in XY]
B = [x - y for x, y in XY]
print(max(max(A) - min(A), max(B) - min(B)))
