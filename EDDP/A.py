n = int(input())
*H, = map(int, input().split())
a, b = 0, abs(H[0]-H[1])
for i in range(2, n):
    a, b = b, min(a+abs(H[i]-H[i-2]), b+abs(H[i]-H[i-1]))
print(b)
