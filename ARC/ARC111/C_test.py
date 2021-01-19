n = int(input())
int0 = lambda x: int(x) - 1
(*a,) = map(int0, input().split())
(*b,) = map(int0, input().split())
(*p,) = map(int0, input().split())
k = int(input())
for _ in range(k):
    i, j = map(int0, input().split())
    p[i], p[j] = p[j], p[i]
assert all(i == p[i] for i in range(n))
