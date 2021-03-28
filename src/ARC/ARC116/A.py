for _ in range(int(input())):
    n = int(input())
    if n % 2:
        print("Odd")
    elif (n // 2) % 2:
        print("Same")
    else:
        print("Even")
