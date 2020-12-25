import heapq
from collections import defaultdict


class HeapBag:
    def __init__(self):
        self.heap = []
        self.count = defaultdict(int)

    def add(self, x):
        heapq.heappush(self.heap, x)
        self.count[x] += 1

    def remove(self, x):
        if self.count[x] == 0:
            return
        self.count[x] -= 1
        while self.heap:
            if self.count[self.heap[0]]:
                break
            heapq.heappop(self.heap)

    def top(self):
        return self.heap[0]

    def __bool__(self):
        return len(self.heap) > 0


m = 2 * 10 ** 5
n, q = map(int, input().split())
a = [None] * n
b = [None] * n
heap_bag_list = [HeapBag() for _ in range(m)]
for i in range(n):
    ai, bi = map(int, input().split())
    a[i] = ai
    b[i] = bi - 1
    heap_bag_list[b[i]].add(-a[i])
max_bag = HeapBag()
for j in range(m):
    if heap_bag_list[j]:
        max_bag.add(-heap_bag_list[j].top())
for _ in range(q):
    c, d = map(int, input().split())
    i, j = c - 1, b[c - 1]
    max_bag.remove(-heap_bag_list[j].top())
    heap_bag_list[j].remove(-a[i])
    if heap_bag_list[j]:
        max_bag.add(-heap_bag_list[j].top())
    j = d - 1
    b[i] = j
    if heap_bag_list[j]:
        max_bag.remove(-heap_bag_list[j].top())
    heap_bag_list[j].add(-a[i])
    max_bag.add(-heap_bag_list[j].top())
    print(max_bag.top())
