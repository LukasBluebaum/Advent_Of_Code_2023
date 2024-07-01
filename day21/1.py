from collections import deque
from decimal import *
import math

with open("in.txt") as file:
    lines = file.readlines()

grid = [list(g.strip()) for g in lines]

start = None
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "S":
            start = (i, j)
            break

f = 26501365
rem = f % len(grid)
xs = [rem + i*len(grid) for i in range(3)]
coeffs = []

for target in xs:
    queue = deque()
    queue.append((start[0], start[1], 0))
    visited = set()
    visited.add((start[0], start[1]))
    count = 0
    while len(queue) > 0:
        ri, rj, d = queue.popleft()
        if d > target:
            break
        if d == target:
            count += 1

        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ii = ri + di
            jj = rj + dj
            ni = (ri + di) % len(grid)
            nj = (rj + dj) % len(grid[0])
            if (ii, jj, d+1) not in visited and grid[ni][nj] != '#':
                queue.append((ii, jj, d+1))
                visited.add((ii, jj, d+1))
    coeffs.append(count)
print(coeffs)

def polynomial(x, ax, ay, bx, by, cx, cy):
    b2 = (by - ay) / (bx - ax)
    tmp = (cy - by) / (cx - bx)
    b3 = (tmp - b2) / (cx - ax)
    return ay + b2 * (x - ax) + b3 * (x - ax) * (x - bx)

args = []
for x, y in zip(xs, coeffs):
    args.append(x)
    args.append(y)
print(polynomial(f, *args))
#print(count + t)
