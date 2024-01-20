s = input()
aset = set()
bset = set()
cset = set()
now = "A"
for c in s:
    if now != c:
        if now == "A":
            now = "B"
        elif now == "B":
            now = "C"
    if now != c:
        if now == "A":
            now = "B"
        elif now == "B":
            now = "C"
    if now == "A":
        aset.add(c)
    elif now == "B":
        bset.add(c)
    elif now == "C":
        cset.add(c)
if (
    (len(aset) == 0 or (len(aset) == 1 and "A" in aset))
    and (len(bset) == 0 or (len(bset) == 1 and "B" in bset))
    and (len(cset) == 0 or (len(cset) == 1 and "C" in cset))
):
    print("Yes")
else:
    print("No")
