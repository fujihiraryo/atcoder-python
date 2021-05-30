int0 = lambda x: int(x) - 1
for _ in range(int(input())):
    n = int(input())
    *p, = map(int0, input().split())
    ans = []
    for i in range(n ** 2):
        if all(p[i] <= p[i + 1] for i in range(n - 1)):
            break
        for j in range(i % 2, n - 1, 2):
            if p[j] > p[j + 1]:
                p[j], p[j + 1] = p[j + 1], p[j]
                ans.append(j)
                break
        else:
            p[j], p[j + 1] = p[j + 1], p[j]
            ans.append(j)
    print(len(ans))
    print(*[i + 1 for i in ans])
