n = input()
for i in range(10):
    if n == n[::-1]:
        print("Yes")
        exit()
    n = "0" + n
print("No")
