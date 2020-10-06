N = int(input())
lst = [{"s": "a", "c": 1}]
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
for n in range(N - 1):
    new_lst = []
    for x in lst:
        for c in range(x["c"] + 1):
            new_s = x["s"] + alphabet[c]
            if c == x["c"]:
                new_c = c + 1
            else:
                new_c = x["c"]
            new_lst.append({"s": new_s, "c": new_c})
    lst = new_lst
for x in lst:
    print(x["s"])
