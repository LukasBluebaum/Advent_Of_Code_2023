from collections import defaultdict
import heapq

with open("in.txt") as file:
    grid = file.readlines()

grid = [[int(a) for a in g.strip()] for g in grid]

dist = defaultdict(lambda: float('inf'))

# 0: Right 1: Down 2: Left 3: Up
directions = {
        0: [(0, 1, 0), (1, 0, 1), (-1, 0, 3)],
        1: [(1, 0, 1), (0, -1, 2), (0, 1, 0)],
        2: [(0, -1 , 2), (1, 0, 1), (-1, 0, 3)],
        3: [(-1, 0, 3), (0, -1, 2), (0, 1, 0)],
}
queue = [(0, 0, 0, 0, 0)]
dist[(0, 0, 0, 0)] = 0

while len(queue) > 0:
    x, i, j, d, c = heapq.heappop(queue)
    if i == len(grid) - 1 and j == len(grid[0]) - 1:
        print(x)
        print(dist[(i, j, d, c)])
        break

    for di, dj, dir_ in directions[d]:
        if dir_ == d and c >= 2:
            continue
        ii = i + di
        jj = j + dj
        if ii < 0 or jj < 0 or ii >= len(grid) or jj >= len(grid[0]):
            continue
        new_distance = dist[(i, j, d, c)] + grid[ii][jj]
        if new_distance < dist[(ii, jj, dir_, (c+1 if dir_ == d else 0))]:
            dist[(ii, jj, dir_, (c+1 if dir_ == d else 0))] = new_distance
            heapq.heappush(queue, (new_distance, ii, jj, dir_, (c+1 if dir_ == d else 0)))


