"""
pを十分大きい素数として, A÷B(mod p)を計算する
"""
A, B, p = map(int, input().split())
print(A * pow(B, p-2, p) % p)
