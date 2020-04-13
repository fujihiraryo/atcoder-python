N = int(input())
S = input()
alphabet = [chr(i) for i in range(65, 65+26)]
T = ""
for s in S:
    i = alphabet.index(s)
    T += alphabet[(i + N) % 26]
print(T)
