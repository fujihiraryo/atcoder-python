from collections import defaultdict

n, m = map(int, input().split())
y_list = defaultdict(list)
for _ in range(m):
    x, y = map(int, input().split())
    y_list[x].append(y)
x_list = list(y_list.keys())
x_list.sort()
y_set = {n}
for x in x_list:
    add_set = set()
    remove_set = set()
    for y in y_list[x]:
        if y not in y_set and (y - 1 in y_set or y + 1 in y_set):
            add_set.add(y)
        if y in y_set and y - 1 not in y_set and y + 1 not in y_set:
            remove_set.add(y)
    for y in add_set:
        y_set.add(y)
    for y in remove_set:
        y_set.remove(y)
print(len(y_set))
