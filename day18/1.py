
def build_grid(lines):
    dirs = {'R': (0, 1), 'L': (0, -1), 'D': (1, 0), 'U': (-1, 0)}
    grid = 0
    points = []
    i, j = 0, 0
    for line in lines:
        points.append((i, j))
        di, dj = dirs[line[0]]
        i += int(line[1]) * di
        j += int(line[1]) * dj
        grid += int(line[1])
    return grid, points


with open("in.txt") as file:
    lines = file.readlines()

lines = [line.strip().split(" ") for line in lines]
grid, points = build_grid(lines)

points = points
area = 0
for i in range(len(points)-1):
    area += (points[i][1] + points[i+1][1]) * ((points[i][0] - points[i+1][0]))
area = abs(area) / 2

print(area + 1 - grid // 2 + grid)

