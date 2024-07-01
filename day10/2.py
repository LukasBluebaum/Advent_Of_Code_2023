from collections import deque


def check(pos, new_pos, symb, new_symb):
    if new_symb == '-':
        if pos[1] < new_pos[1] and symb in {'L', '-', 'F'}:
            return True
        elif pos[1] > new_pos[1] and symb in {'J', '-', '7'}:
            return True
        else:
            return False
    elif new_symb == '|':
        if pos[0] < new_pos[0] and symb in {'|', 'F', '7'}:
            return True
        elif pos[0] > new_pos[0] and symb in {'J', 'L', '|'}:
            return True
        else:
            return False
    elif new_symb == 'L':
        if pos[1] > new_pos[1] and symb in {'J', '-', '7'}:
            return True
        elif pos[0] < new_pos[0] and symb in {'7', 'F', '|'}:
            return True
        else:
            return False
    elif new_symb == 'J':
        if pos[1] < new_pos[1] and symb in {'F', '-', 'L'}:
            return True
        elif pos[0] < new_pos[0] and symb in {'7', 'F', '|'}:
            return True
        else:
            return False
    elif new_symb == '7':
        if pos[1] < new_pos[1] and symb in {'F', '-', 'L'}:
            return True
        elif pos[0] > new_pos[0] and symb in {'J', 'L', '|'}:
            return True
        else:
            return False
    elif new_symb == 'F':
        if pos[1] > new_pos[1] and symb in {'J', '-', '7'}:
            return True
        elif pos[0] > new_pos[0] and symb in {'J', 'L', '|'}:
            return True
        else:
            return False
    return False


def bfs(start, grid):
    queue = deque()
    visited = {}
    prev = {}
    for s in ['|', '-', 'L', 'J', '7', 'F']:
        queue.append((*start, s, 0))
        visited[(*start, s)] = 0

    res = 0
    loop_ends = None
    while len(queue) > 0:
        i, j, s, d = queue.popleft()

        for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            ni = i + di
            nj = j + dj
            if ni < 0 or nj < 0 or ni >= len(grid) or nj >= len(grid[0]):
                continue
            symb = grid[i][j] if (i, j) != start else s
            new_symb = grid[ni][nj] if (ni, nj) != start else s
            if check((i, j), (ni, nj), symb, new_symb):
                if (ni, nj, s) in visited:
                    if res < d + visited[(ni, nj, s)]:
                        res = d + visited[(ni, nj, s)]
                        loop_ends = ((i, j, s), (ni, nj, s))
                else:
                    prev[(ni, nj, s)] = (i, j, s)
                    queue.append((ni, nj, s, d + 1))
                    visited[(ni, nj, s)] = d + 1
    return res, loop_ends, prev


def get_path(prev, node):
    path = []
    while node in prev:
        path.append((node[0], node[1]))
        node = prev[node]
    return path


with open("in.txt") as file:
    grid = file.readlines()

grid = [list(g.strip()) for g in grid]

start = None
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'S':
            start = (i, j)


res, loop_ends, prev = bfs(start, grid)
print((res + 1) // 4)

p1 = get_path(prev, loop_ends[0])
points = [start] + [p for p in p1 if grid[p[0]][p[1]] in {'F', 'L', 'J', '7'}] + [start]

area = 0
for i in range(len(points)-1):
    area += (points[i][1] + points[i+1][1]) * (points[i][0] - points[i+1][0])
area = abs(area) / 2

print(area + 1 - (len(p1)+1) // 2)


