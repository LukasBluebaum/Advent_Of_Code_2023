
def build_grid(lines):
    dirs = {'0': (0, 1), '2': (0, -1), '1': (1, 0), '3': (-1, 0)}
    grid = 0
    points = []
    i, j = 0, 0
    for line in lines:
        points.append((i, j))
        d = line[2][-2]
        count = int(line[2][2:-2], 16)
        di, dj = dirs[d]
        i += count * di
        j += count * dj
        grid += count
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

