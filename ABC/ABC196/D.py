from copy import deepcopy
from itertools import product


def solve(grid, a, b):
    if a == 0 and b == 0:
        return 1
    h, w = len(grid), len(grid[0])
    for i, j in product(range(h), range(w)):
        if grid[i][j] == 0:
            break
    res = 0
    if a > 0 and i + 1 < h and grid[i + 1][j] == 0:
        new_grid = deepcopy(grid)
        new_grid[i][j] = 1
        new_grid[i + 1][j] = 1
        res += solve(new_grid, a - 1, b)
    if a > 0 and j + 1 < w and grid[i][j + 1] == 0:
        new_grid = deepcopy(grid)
        new_grid[i][j] = 1
        new_grid[i][j + 1] = 1
        res += solve(new_grid, a - 1, b)
    if b > 0:
        new_grid = deepcopy(grid)
        new_grid[i][j] = 1
        res += solve(new_grid, a, b - 1)
    return res


h, w, a, b = map(int, input().split())
grid = [[0] * w for _ in range(h)]
print(solve(grid, a, b))
