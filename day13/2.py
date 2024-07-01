
def compare_rows(grid, a, b):
    return sum(aa != bb for aa, bb in zip(grid[a], grid[b]))

def compare_cols(grid, a, b):
    return sum(grid[i][a] != grid[i][b] for i in range(len(grid)))

def dfs_rows(grid, i, j):
    if i < 0 or j >= len(grid):
        return 0
    return compare_rows(grid, i, j) + dfs_rows(grid, i-1, j+1)

def dfs_cols(grid, i, j):
    if i < 0 or j >= len(grid[0]):
        return 0
    return compare_cols(grid, i, j) + dfs_cols(grid, i-1, j+1)

def find(grid):
    for i in range(len(grid)-1):
        if dfs_rows(grid, i, i+1) == 1:
            return (i + 1) * 100

    for i in range(len(grid[0])-1):
        if dfs_cols(grid, i, i+1) == 1:
            return i + 1


with open("in.txt") as file:
    lines = file.read()

grids = lines.strip().split('\n\n')
grids = [[list(g) for g in grid.split("\n")] for grid in grids]


res = 0
for grid in grids:
    res += find(grid)
print(res)



