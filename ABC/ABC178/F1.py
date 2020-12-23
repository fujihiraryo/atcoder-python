n = int(input())
(*a,) = map(int, input().split())
(*b,) = map(int, input().split())
b.reverse()
j, k = 0, n - 1
for i in range(n):
    if a[i] != b[i]:
        continue
    if i % 2 == 0:
        b[i], b[j] = b[j], b[i]
        j += 1
    else:
        b[i], b[k] = b[k], b[i]
        k -= 1
if all(a[i] != b[i] for i in range(n)):
    print("Yes")
    print(*b)
else:
    print("No")
