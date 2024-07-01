
def north(grid):
    res = 0
    for j in range(len(grid[0])):
        last = 0
        for i in range(len(grid)):
            if grid[i][j] == 'O':
                if i > last:
                    res += len(grid) - last
                else:
                    res += len(grid) - i
                last += 1
            elif grid[i][j] == '#':
                last = i + 1
    return res


with open("in.txt") as file:
    grid = file.readlines()

grid = [list(g.strip()) for g in grid]
print(north(grid))
