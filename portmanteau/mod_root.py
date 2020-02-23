# zはmod pで1のn乗根
n = 2 ** 17
p = 149 * n + 1
z = 770
print(pow(z, n, p))
print(pow(z, p-1, p))
