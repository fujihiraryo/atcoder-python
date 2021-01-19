import heapq
from collections import defaultdict


class PriorityQuene:
    def __init__(self):
        self.heap = []
        self.count = defaultdict(int)

    def push(self, x):
        heapq.heappush(self.heap, x)
        self.count[x] += 1

    def pop(self):
        res = self.top()
        self.remove(res)
        return res

    def top(self):
        return self.heap[0]

    def remove(self, x):
        if self.count[x] == 0:
            return
        self.count[x] -= 1
        while self.heap:
            if self.count[self.top()]:
                break
            heapq.heappop(self.heap)

    def __bool__(self):
        return bool(self.heap)


n = int(input())
int0 = lambda x: int(x) - 1
(*a,) = map(int0, input().split())
(*b,) = map(int0, input().split())
(*p,) = map(int0, input().split())
if any(a[i] <= b[p[i]] and i != p[i] for i in range(n)):
    print(-1)
    exit()
q = [None] * n
for i in range(n):
    q[p[i]] = i
heap = PriorityQuene()
for i in range(n):
    heap.push((a[i], i))
ans = []
while heap:
    _, i = heap.pop()
    j = i
    while q[j] != i:
        ans.append(j)
        j = q[j]
        heap.remove((a[j], j))
print(len(ans))
for j in ans:
    print(j + 1, q[j] + 1)
