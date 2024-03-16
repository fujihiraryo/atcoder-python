from collections import defaultdict


counter = defaultdict(int)
s = input()
n = len(s)
ans = n * (n - 1) // 2
flag = False
for i in range(n):
    if not flag and counter[s[i]] > 1:
        ans -= counter[s[i]]
    elif flag and counter[s[i]] > 0:
        ans -= counter[s[i]]
    counter[s[i]] += 1
    if counter[s[i]] > 1:
        flag = True
print(ans)

# st = set()
# for i in range(n - 1):
#     for j in range(i + 1, n):
#         t = list(s[:])
#         t[i], t[j] = t[j], t[i]
#         st.add("".join(t))
# print(len(st))
