n = int(input())
(*A,) = map(int, input().split())
s = 0
for a in A:
    s = s ^ a
X = [s ^ a for a in A]
print(*X)
