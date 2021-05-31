INF = 10 ** 10
int0 = lambda x: int(x) - 1
n, m = map(int, input().split())
author_paper = [[] for _ in range(n)]
paper_author = [[] for _ in range(m)]
for j in range(m):
    input()
    for i in map(int0, input().split()):
        author_paper[i].append(j)
        paper_author[j].append(i)
author_checked = [0] * n
paper_checked = [0] * m
number = [INF] * n
number[0] = 0
queue = [0]
for i in queue:
    author_checked[i] = 1
    for j in author_paper[i]:
        if paper_checked[j]:
            continue
        paper_checked[j] = 1
        t = min(number[x] for x in paper_author[j])
        for x in paper_author[j]:
            number[x] = min(number[x], t + 1)
            if not author_checked[x]:
                queue.append(x)
for i in range(n):
    print(number[i] if number[i] < INF else -1)
