n = int(input())
(*d,) = map(int, input().split())
ans = 0
for i in range(n):
    for j in range(1, d[i] + 1):
        if (
            len(set(str(i + 1))) == 1
            and len(set(str(j))) == 1
            and set(str(i + 1)) == set(str(j))
        ):
            ans += 1
print(ans)
