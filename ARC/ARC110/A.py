i = 2 ** 4 * 3 ** 3 * 5 ** 2 * 7 * 11 * 13 * 17 * 19 * 23 * 29 + 1
print(i)
print(all(i % j == 1 for j in range(2, 30 + 1)))
