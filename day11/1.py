
def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

with open("in.txt") as file:
    grid = file.readlines()

grid = [list(g.strip()) for g in grid]

rows = {i for i in range(len(grid)) if all(j == '.' for j in grid[i])}
cols = {j for j in range(len(grid[0])) if all(grid[i][j] == '.' for i in range(len(grid)))}
galaxies = [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == '#']

expansion = 10**6
res = 0
for a in range(len(galaxies)):
    for b in range(a+1, len(galaxies)):
        aa = galaxies[a]
        bb = galaxies[b]
        res += manhattan(aa, bb)
        x, y = min(aa[0], bb[0]), max(aa[0], bb[0])
        res += len(rows & set(range(x, y))) * (expansion-1)
        x, y = min(aa[1], bb[1]), max(aa[1], bb[1])
        res += len(cols & set(range(x, y))) * (expansion-1)

print(res)

