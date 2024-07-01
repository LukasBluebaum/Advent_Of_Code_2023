import sys
sys.setrecursionlimit(15000)

def handle_dot(i, j, d):
    if d == 0:
        return i, j+1, d
    elif d == 1:
        return i+1, j, d
    elif d == 2:
        return i, j-1, d
    elif d == 3:
        return i-1, j, d


def handle_left_mirror(i, j, d):
    if d == 0:
        return i-1, j, 3
    elif d == 1:
        return i, j-1, 2
    elif d == 2:
        return i+1, j, 1
    elif d == 3:
        return i, j+1, 0


def handle_right_mirror(i, j, d):
    if d == 0:
        return i+1, j, 1
    elif d == 1:
        return i, j+1, 0
    elif d == 2:
        return i-1, j, 3
    elif d == 3:
        return i, j-1, 2


# 0: right 1: down 2: left 3: up
def dfs(i, j, direction, visited, energized, grid):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) \
            or (i, j, direction) in visited:
        return
    visited.add((i, j, direction))
    energized.add((i, j))

    c = grid[i][j]
    if c == '.':
        i, j, d = handle_dot(i, j, direction)
        dfs(i, j, direction, visited, energized, grid)
    elif c == '/':
        i, j, d = handle_left_mirror(i, j, direction)
        dfs(i, j, d, visited, energized, grid)
    elif c == '\\':
        i, j, d = handle_right_mirror(i, j, direction)
        dfs(i, j, d, visited, energized, grid)
    elif c == '-':
        if direction == 0:
            dfs(i, j+1, direction, visited, energized, grid)
        elif direction == 2:
            dfs(i, j-1, direction, visited, energized, grid)
        elif direction == 1 or direction == 3:
            dfs(i, j+1, 0, visited, energized, grid)
            dfs(i, j-1, 2, visited, energized, grid)
    elif c == '|':
        if direction == 1:
            dfs(i+1, j, direction, visited, energized, grid)
        elif direction == 3:
            dfs(i-1, j, direction, visited, energized, grid)
        elif direction == 0 or direction == 2:
            dfs(i+1, j, 1, visited, energized, grid)
            dfs(i-1, j, 3, visited, energized, grid)



with open("in.txt") as file:
    grid = file.readlines()

grid = [list(g.strip()) for g in grid]

energized = set()
dfs(0, 0, 0, set(), energized, grid)

print(len(energized))

