N = int(input())
(*P,) = map(int, input().split())
minimun = N + 1
count = 0
for p in P:
    if p < minimun:
        minimun = p
        count += 1
print(count)
