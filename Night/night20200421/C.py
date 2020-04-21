import bisect
n = int(input())
*L, = map(int, input().split())
# n = 4
# L = [3, 4, 2, 1]
# n = 7
# L = [218, 786, 704, 233, 645, 728, 389]
L.sort()
c = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        c += bisect.bisect_left(L, L[i]+L[j])-(j+1)
print(c)
