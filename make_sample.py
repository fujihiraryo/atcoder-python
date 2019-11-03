import sys
sys.stdout = open('sample.txt', 'w')

# 以下の出力がサンプルファイルになる

N = 10**3

print(N)
for n in range(N):
    print(*[1 for i in range(n)])
