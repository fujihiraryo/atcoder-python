n, p = map(int, input().split())
(*A,) = map(int, input().split())
c = 0
for i in range(n):
    if p >= A[i]:
        p -= A[i]
        c += 1
    else:
        break
print(c)
