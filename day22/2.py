from collections import defaultdict


with open("in.txt") as file:
    lines = file.readlines()

cubes = []
for line in lines:
    a, b = line.split("~")
    a = [int(x) for x in a.strip().split(",")]
    b = [int(x) for x in b.strip().split(",")]
    cubes.append((a, b))

cubes = sorted(cubes, key=lambda a: a[1][-1])
pos = defaultdict(list)

all_below = defaultdict(set)
above = defaultdict(set)

for idx, cube in enumerate(cubes):
    x, y, z = cube[0]
    x2, y2, z2 = cube[1]

    coords = []
    if y != y2:
        coords = [(x, i) for i in range(y, y2+1)]
    elif x != x2:
        coords = [(i, y) for i in range(x, x2+1)]
    else:
        coords = [(x, y)]

    counts = []
    current_max = 0
    for c in coords:
        if len(pos[c]) > 0 and pos[c][-1][1] > current_max:
            counts = [pos[c][-1]]
            current_max = pos[c][-1][1]
        elif len(pos[c]) > 0 and pos[c][-1][1] == current_max:
            counts.append(pos[c][-1])

    below = {x[0] for x in counts}
    all_below[idx] = below
    for b in below:
        above[b].add(idx)

    if len(below) == 1:
        found.add(list(below)[0])

    height = (max(x[1] for x in counts) if len(counts) > 0 else 0) + (z2 - z + 1)
    for c in coords:
        pos[c].append((idx, height))


def find(node, current):
    for a in above[node]:
        if a not in current and len(all_below[a] - current) == 0:
            current.add(a)
            find(a, current)

s = 0
for idx in range(len(cubes)):
    current = {idx}
    find(idx, current)
    s += len(current) - 1
print(s)
