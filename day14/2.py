
def north(grid):
    for j in range(len(grid[0])):
        last = 0
        for i in range(len(grid)):
            if grid[i][j] == 'O':
                if i > last:
                    grid[last][j] = 'O'
                    grid[i][j] = '.'
                last += 1
            elif grid[i][j] == '#':
                last = i + 1

def south(grid):
    for j in range(len(grid[0])):
        last = len(grid) - 1
        for i in range(len(grid)-1, -1, -1):
            if grid[i][j] == 'O':
                if i < last:
                    grid[last][j] = 'O'
                    grid[i][j] = '.'
                last -= 1
            elif grid[i][j] == '#':
                last = i - 1

def west(grid):
    for i in range(len(grid)):
        last = 0
        for j in range(len(grid[0])):
            if grid[i][j] == 'O':
                if j > last:
                    grid[i][last] = 'O'
                    grid[i][j] = '.'
                last += 1
            elif grid[i][j] == '#':
                last = j + 1

def east(grid):
    for i in range(len(grid)):
        last = len(grid[0]) - 1
        for j in range(len(grid[0])-1, -1, -1):
            if grid[i][j] == 'O':
                if j < last:
                    grid[i][last] = 'O'
                    grid[i][j] = '.'
                last -= 1
            elif grid[i][j] == '#':
                last = j - 1

def calculate(grid):
    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'O':
                res += len(grid) - i
    return res


with open("in.txt") as file:
    grid = file.readlines()

grid = [list(g.strip()) for g in grid]

seen = {}
i = 0
found = False
limit = 10**9
while i < limit:
    north(grid)
    west(grid)
    south(grid)
    east(grid)
    i += 1
    key = tuple(tuple(x) for x in grid)
    if key in seen and not found:
        i = limit - (limit - seen[key]) % (i - seen[key])
        found = True
    else:
        seen[key] = i

print(calculate(grid))
