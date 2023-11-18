import heapq
from collections import defaultdict

n, m = map(int, input().split())
(*a,) = map(int, input().split())

heap = []
cnt = defaultdict(int)
for i in range(m):
    cnt[a[i]] += 1
    heapq.heappush(heap, (-cnt[a[i]], a[i]))
    print(heap[0][1])
