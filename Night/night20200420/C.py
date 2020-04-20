n, k = map(int, input().split())
*A, = map(int, input().split())
# n, k = 10, 3
# A = [5, 1, 3, 2, 4, 1, 1, 2, 3, 4]
# n, k = 4, 4
# A = [1, 1, 2, 2]
D = {}
for a in A:
    try:
        D[a] += 1
    except:
        D[a] = 1
D = sorted(D.values())
print(sum(D[:len(D)-k]))
