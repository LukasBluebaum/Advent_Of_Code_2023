from collections import deque, defaultdict

with open("in.txt") as file:
    grid = file.readlines()

grid = [list(g.strip()) for g in grid]

edges = defaultdict(set)
for i in range(1, len(grid)-1):
    for j in range(1, len(grid[0])-1):
        if grid[i][j] != '#':
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni = i + di
                nj = j + dj
                if grid[ni][nj] != '#':
                    edges[(i, j)].add((ni, nj, 1))
                    edges[(ni, nj)].add((i, j, 1))

edges[(0, 1)] = {(1, 1, 1)}
edges[(len(grid)-1, len(grid[0])-2)] = {(len(grid)-2, len(grid[0])-2, 1)}

while any(len(nbs) == 2 for _, nbs in edges.items()):
    for node, nbs in edges.items():
        if len(nbs) == 2:
            l, r = nbs
            edges[(l[0], l[1])].add((r[0], r[1], l[2] + r[2]))
            edges[(r[0], r[1])].add((l[0], l[1], l[2] + r[2]))
            edges[(l[0], l[1])].remove((node[0], node[1], l[2]))
            edges[(r[0], r[1])].remove((node[0], node[1], r[2]))
            edges[node] = set()

queue = deque()
queue.append((0, 1, 0, {(0, 1)}))
res = 0
while len(queue) > 0:
    i, j, d, visited = queue.popleft()
    if i == len(grid) - 1 and j == len(grid[0]) - 2:
        res = max(res, d)
        continue

    for ni, nj, dd in edges[(i, j)]:
        if ni < 0 or nj < 0 or ni >= len(grid) or nj >= len(grid[0]) or grid[ni][nj] == '#':
            continue

        if (ni, nj) not in visited:
            queue.append((ni, nj, d+dd, visited | {(ni, nj)}))

print(res)
