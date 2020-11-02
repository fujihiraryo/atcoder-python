def keta_counter(string):
    ret = [0] * 10
    for s in string:
        ret[int(s)] += 1
    return ret


def a_in_b(a, b):
    return all([a[i] <= b[i] for i in range(10)])


S = input()
if len(S) < 3:
    if int(S) % 8 == 0 or int(S[::-1]) % 8 == 0:
        print("Yes")
    else:
        print("No")
    exit()
S = keta_counter(S)
a_list = []
for i in range(100, 1000):
    if i % 8 == 0 and str(i).count("0") == 0:
        a_list.append(keta_counter(str(i)))


if any([a_in_b(a, S) for a in a_list]):
    print("Yes")
else:
    print("No")
