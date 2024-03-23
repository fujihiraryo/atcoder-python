from collections import defaultdict

n = int(input())
(*a,) = map(int, input().split())


def force():
    ans = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            cnt = defaultdict(int)
            for x in a[i:j]:
                cnt[x] += 1
            for x in cnt:
                if cnt[x] == 1:
                    ans += 1
                    break
    return ans


print(force())
