N = int(input())
A = [list(map(int, input().split())) for n in range(N)]
print(sum([sum(a) for a in A]))
