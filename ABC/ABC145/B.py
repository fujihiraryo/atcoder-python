N = int(input())
S = input()
print(["No", "Yes"][int(S[: N // 2] == S[N // 2 :])])
