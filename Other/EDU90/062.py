n = int(input())
a = [0] * n
b = [0] * n
for i in range(n):
    a[i], b[i] = map(int, input().split())
# a[i]->i, b[i]->i に辺を張る
graph = [[] for _ in range(n)]
stack = []
for i in range(n):
    graph[a[i] - 1].append(i)
    graph[b[i] - 1].append(i)
    if a[i] - 1 == i or b[i] - 1 == i:
        stack.append(i)
ans = []
done = [0] * n
while stack:
    i = stack.pop()
    if done[i]:
        continue
    ans.append(i)
    done[i] = 1
    for j in graph[i]:
        stack.append(j)
if len(ans) != n:
    print(-1)
    exit()
for i in ans[::-1]:
    print(i + 1)
