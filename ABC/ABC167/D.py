n, k = map(int, input().split())
*A, = map(int, input().split())
# n, k = 6, 727202214173249351
# A = [6, 5, 2, 5, 3, 2]
# n, k = 2, 1
# A = [1, 3]
# n, k = 3, 3
# A = [2, 3, 3]
A = [a - 1 for a in A]
now = 0
V = [False for i in range(n)]
V[0] = 0
L = [now]
cnt = 0
while not V[A[now]]:
    cnt += 1
    now = A[now]
    L.append(now)
    V[now] = cnt
a = V[A[now]]
b = cnt - a + 1
if k < cnt:
    print(L[k] + 1)
    exit()
print(L[(k - a) % b + a] + 1)
