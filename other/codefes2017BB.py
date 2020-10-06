n = int(input())
(*D,) = map(int, input().split())
m = int(input())
(*T,) = map(int, input().split())
D.sort()
T.sort()
j = 0
for i in range(n):
    if j == m:
        break
    if D[i] == T[j]:
        j += 1
if j == m:
    print("YES")
else:
    print("NO")
