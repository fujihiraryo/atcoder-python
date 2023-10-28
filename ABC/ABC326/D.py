from itertools import permutations


def overlapABC(s, t):
    for i in range(len(s)):
        if s[i] in ("A", "B", "C"):
            if s[i] == t[i]:
                return True
    return False


n = int(input())
R = input()
C = input()

if n == 5:
    for row0 in permutations("ABC..", 5):
        if R[0] != "".join(row0).replace(".", "")[0]:
            continue
        for row1 in permutations("ABC..", 5):
            if overlapABC(row0, row1):
                continue
            if R[1] != "".join(row1).replace(".", "")[0]:
                continue
            for row2 in permutations("ABC..", 5):
                if overlapABC(row0, row2) or overlapABC(row1, row2):
                    continue
                if R[2] != "".join(row2).replace(".", "")[0]:
                    continue
                for row3 in permutations("ABC..", 5):
                    if (
                        overlapABC(row0, row3)
                        or overlapABC(row1, row3)
                        or overlapABC(row2, row3)
                    ):
                        continue
                    if R[3] != "".join(row3).replace(".", "")[0]:
                        continue
                    for row4 in permutations("ABC..", 5):
                        if (
                            overlapABC(row0, row4)
                            or overlapABC(row1, row4)
                            or overlapABC(row2, row4)
                            or overlapABC(row3, row4)
                        ):
                            continue
                        if R[4] != "".join(row4).replace(".", "")[0]:
                            continue
                        col0 = row0[0] + row1[0] + row2[0] + row3[0] + row4[0]
                        col1 = row0[1] + row1[1] + row2[1] + row3[1] + row4[1]
                        col2 = row0[2] + row1[2] + row2[2] + row3[2] + row4[2]
                        col3 = row0[3] + row1[3] + row2[3] + row3[3] + row4[3]
                        col4 = row0[4] + row1[4] + row2[4] + row3[4] + row4[4]
                        if C[0] != "".join(col0).replace(".", "")[0]:
                            continue
                        if C[1] != "".join(col1).replace(".", "")[0]:
                            continue
                        if C[2] != "".join(col2).replace(".", "")[0]:
                            continue
                        if C[3] != "".join(col3).replace(".", "")[0]:
                            continue
                        if C[4] != "".join(col4).replace(".", "")[0]:
                            continue
                        print("Yes")
                        print("".join(row0))
                        print("".join(row1))
                        print("".join(row2))
                        print("".join(row3))
                        print("".join(row4))
                        exit()
    print("No")


if n == 4:
    for row0 in permutations("ABC.", 4):
        if R[0] != "".join(row0).replace(".", "")[0]:
            continue
        for row1 in permutations("ABC.", 4):
            if overlapABC(row0, row1):
                continue
            if R[1] != "".join(row1).replace(".", "")[0]:
                continue
            for row2 in permutations("ABC.", 4):
                if overlapABC(row0, row2) or overlapABC(row1, row2):
                    continue
                if R[2] != "".join(row2).replace(".", "")[0]:
                    continue
                for row3 in permutations("ABC.", 4):
                    if (
                        overlapABC(row0, row3)
                        or overlapABC(row1, row3)
                        or overlapABC(row2, row3)
                    ):
                        continue
                    if R[3] != "".join(row3).replace(".", "")[0]:
                        continue
                    col0 = row0[0] + row1[0] + row2[0] + row3[0]
                    col1 = row0[1] + row1[1] + row2[1] + row3[1]
                    col2 = row0[2] + row1[2] + row2[2] + row3[2]
                    col3 = row0[3] + row1[3] + row2[3] + row3[3]
                    if C[0] != "".join(col0).replace(".", "")[0]:
                        continue
                    if C[1] != "".join(col1).replace(".", "")[0]:
                        continue
                    if C[2] != "".join(col2).replace(".", "")[0]:
                        continue
                    if C[3] != "".join(col3).replace(".", "")[0]:
                        continue
                    print("Yes")
                    print("".join(row0))
                    print("".join(row1))
                    print("".join(row2))
                    print("".join(row3))
                    exit()
    print("No")


if n == 3:
    for row0 in permutations("ABC", 3):
        if R[0] != "".join(row0).replace(".", "")[0]:
            continue
        for row1 in permutations("ABC", 3):
            if overlapABC(row0, row1):
                continue
            if R[1] != "".join(row1).replace(".", "")[0]:
                continue
            for row2 in permutations("ABC", 3):
                if overlapABC(row0, row2) or overlapABC(row1, row2):
                    continue
                if R[2] != "".join(row2).replace(".", "")[0]:
                    continue
                col0 = row0[0] + row1[0] + row2[0]
                col1 = row0[1] + row1[1] + row2[1]
                col2 = row0[2] + row1[2] + row2[2]
                if C[0] != "".join(col0).replace(".", "")[0]:
                    continue
                if C[1] != "".join(col1).replace(".", "")[0]:
                    continue
                if C[2] != "".join(col2).replace(".", "")[0]:
                    continue
                print("Yes")
                print("".join(row0))
                print("".join(row1))
                print("".join(row2))
                exit()
    print("No")
