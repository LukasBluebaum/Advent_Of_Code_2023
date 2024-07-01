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


with open("in.txt") as file:
    grid = file.readlines()

grid = [list(g.strip()) for g in grid]

start = None
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'S':
            start = (i, j)
            break

queue = deque()
visited = {}
for s in {'|', '-', 'L', 'J', '7', 'F'}:
    queue.append((*start, s, 0))
    visited[(*start, s)] = 0

res = 0
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
                res = max(res, d, visited[(ni, nj, s)])
            else:
                queue.append((ni, nj, s, d + 1))
                visited[(ni, nj, s)] = d + 1

print(res)
print((res + 1) // 2)



