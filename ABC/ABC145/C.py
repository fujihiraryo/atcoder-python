N = int(input())
L = [tuple(map(int, input().split())) for n in range(N)]
Roads = []
for n in range(N):
    for m in range(n + 1, N):
        distance = ((L[n][0] - L[m][0]) ** 2 + (L[n][1] - L[m][1]) ** 2) ** 0.5
        Roads.append(distance)
mean = sum(Roads) / len(Roads)
print(mean * (N - 1))
