n = int(input())
lst = [0] * 24
for _ in range(n):
    w, x = map(int, input().split())
    for start in range(24):
        if 9 <= (start + x) % 24 < 18:
            lst[start] += w
print(max(lst))
