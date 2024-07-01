from collections import deque


with open("in.txt") as file:
    grid = file.readlines()

grid = [list(g.strip()) for g in grid]
dirs = {'>': (0, 1), 'v': (1, 0), '^': (-1, 0), '<': (0, -1)}

queue = deque()
queue.append((0, 1, 0, {(0, 1)}))

while len(queue) > 0:
    i, j, d, visited = queue.popleft()
    if i == len(grid) - 1 and j == len(grid[0]) - 2:
        print(d)
        continue
    if grid[i][j] != "#" and grid[i][j] != '.':
        di, dj = dirs[grid[i][j]]
        ni = i + di
        nj = j + dj
        if (ni, nj) not in visited:
            queue.append((ni, nj, d+1, visited | {(ni, nj)}))
        continue

    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        ni = i + di
        nj = j + dj

        if ni < 0 or nj < 0 or ni >= len(grid) or nj >= len(grid[0]) or grid[ni][nj] == '#':
            continue
        if (ni, nj) not in visited:
            queue.append((ni, nj, d+1, visited | {(ni, nj)}))
