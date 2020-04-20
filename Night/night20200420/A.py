A = [int(input()) for i in range(5)]
# A = [101, 86, 119, 108, 57]
# A = [29, 20, 7, 35, 120]
# A = [123, 123, 123, 123, 123]
B = [(10-a % 10) % 10 for a in A]
C = [-(-a//10)*10 for a in A]
print(sum(C)-max(B))
