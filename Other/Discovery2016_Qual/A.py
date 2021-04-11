w = int(input())
s = "DiscoPresentsDiscoveryChannelProgrammingContest2016"
n = len(s)
for i in range(-(-n // w)):
    print(s[i * w : (i + 1) * w])
