n = int(input())
(*p,) = map(int, input().split())
if all(p[k] < p[k + 1] for k in range(n - 1)):
    print("YES")
    exit()
for i in range(n - 1):
    for j in range(i + 1, n):
        p[i], p[j] = p[j], p[i]
        if all(p[k] < p[k + 1] for k in range(n - 1)):
            print("YES")
            exit()
        else:
            p[i], p[j] = p[j], p[i]
print("NO")
