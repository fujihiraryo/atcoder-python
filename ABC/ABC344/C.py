n = int(input())
(*a,) = map(int, input().split())
m = int(input())
(*b,) = map(int, input().split())
l = int(input())
(*c,) = map(int, input().split())
q = int(input())
(*x,) = map(int, input().split())


s = set()
for i in range(n):
    for j in range(m):
        for k in range(l):
            s.add(a[i] + b[j] + c[k])


for i in range(q):
    print("Yes" if x[i] in s else "No")
