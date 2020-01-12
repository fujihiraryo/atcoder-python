alphabet = [chr(ord('a') + i) for i in range(26)]
C = input()
for i in range(25):
    if alphabet[i] == C:
        print(alphabet[i+1])
