import heapq

N, M = map(int, input().split())
work_list = [[] for m in range(M + 1)]
for n in range(N):
    a, b = map(int, input().split())
    if a <= M:
        work_list[a].append(-b)

Q = [0 for m in range(M)]
ans = 0
for m in range(1, M+1):
    for work in work_list[m]:
        heapq.heappush(Q, work)
    ans += heapq.heappop(Q)

print(-ans)
