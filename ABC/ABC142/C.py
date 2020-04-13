N = int(input())
A = list(map(int, input().split()))

B = [(a, i + 1) for i, a in enumerate(A)]
B.sort()

print(*[b[1] for b in B])
