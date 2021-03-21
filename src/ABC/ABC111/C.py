from collections import Counter

n = int(input())
(*a,) = map(int, input().split())
cnt0 = Counter(a[0::2])
cnt1 = Counter(a[1::2])
keys0 = list(cnt0.keys())
keys1 = list(cnt1.keys())
keys0.sort(key=lambda x: -cnt0[x])
keys1.sort(key=lambda x: -cnt1[x])
if keys0[0] == keys1[0]:
    if len(keys0) == 1 and len(keys1) == 1:
        print(n // 2)
        exit()
    if len(keys0) == 1:
        print(n // 2 - cnt1[keys1[1]])
        exit()
    if len(keys1) == 1:
        print(n // 2 - cnt0[keys0[1]])
        exit()
    print(min(n - cnt0[keys0[0]] - cnt1[keys1[1]], n - cnt0[keys0[1]] - cnt1[keys1[0]]))
    exit()
print(n - cnt0[keys0[0]] - cnt1[keys1[0]])
