from itertools import permutations, product


n, h, w = map(int, input().split())
tiles = []
for i in range(n):
    a, b = map(int, input().split())
    tiles.append((a, b))


def check(tile_order, turns):
    grid = [[0] * w for _ in range(h)]
    i, j = 0, 0
    for k in range(n):
        a, b = tile_order[k]
        if turns[k]:
            a, b = b, a
        # まだ埋まっていない最初のi,jを探す
        for x in range(i * w + j, h * w):
            if grid[x // w][x % w] == 0:
                i, j = x // w, x % w
                break
        # はみ出ないかチェック
        if i + a > h or j + b > w:
            return False
        # 重ならないかチェック
        if any(grid[ia][jb] for ia in range(i, i + a) for jb in range(j, j + b)):
            return False
        for ia in range(i, i + a):
            for jb in range(j, j + b):
                grid[ia][jb] = 1
        if all(grid[i][j] for i in range(h) for j in range(w)):
            return True


turns_list = list(product((False, True), repeat=n))

# タイルの順番を固定
for tile_order in permutations(tiles, n):
    # 各タイルの縦置き・横置きを固定
    for turns in turns_list:
        if check(tile_order, turns):
            print("Yes")
            exit()
print("No")
