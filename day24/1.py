
def intersection(x1, y1, x2, y2, x3, y3, x4, y4):
    dem = (x1-x2) * (y3-y4) - (y1-y2) * (x3-x4)
    if dem == 0:
        return None, None
    numx = (x1*y2 - y1*x2)*(x3-x4) - (x1-x2) * (x3*y4 - y3*x4)
    numy = (x1*y2 - y1*x2)*(y3-y4) - (y1-y2) * (x3*y4 - y3*x4)
    return numx/dem, numy/dem


with open("in.txt") as file:
    lines = file.readlines()

stones = []
for line in lines:
    pos, vel = line.split("@")
    pos = [int(a) for a in pos.strip().split(", ")]
    vel = [int(a) for a in vel.strip().split(", ")]
    stones.append((pos, vel))

# l = 7
# h = 27
l = 200000000000000
h = 400000000000000

res = 0
for i in range(len(stones)):
    for j in range(i+1, len(stones)):
        x1, y1 = stones[i][0][0], stones[i][0][1]
        x2, y2 = x1 + stones[i][1][0], y1 + stones[i][1][1]
        x3, y3 = stones[j][0][0], stones[j][0][1]
        x4, y4 = x3 + stones[j][1][0], y3 + stones[j][1][1]

        dx, dy = intersection(x1, y1, x2, y2, x3, y3, x4, y4)
        if dx is None:
            continue
        future_a = (dx > x1) == (x2 > x1)
        future_b = (dx > x3) == (x4 > x3)
        if l <= dx <= h and l <= dy <= h and future_a and future_b:
            res += 1

print(res)
