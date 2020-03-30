# 部分リストのリスト
def all_sublist(lst):
    lstlst = []
    for i in range(2**len(lst)):
        sublst = []
        for j in range(len(lst)):
            if (i >> j) & 1 == 1:
                sublst.append(lst[j])
        lstlst.append(sublst)
    return lstlst