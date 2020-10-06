N = int(input())
(*X,) = map(int, input().split())
g = round(sum(X) / N)
print(sum([(x - g) ** 2 for x in X]))
