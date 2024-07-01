import re

with open('in.txt') as file:
    lines = file.readlines()

seeds = re.findall(r'\d+', lines[0])
seeds = [int(s) for s in seeds]

maps = []
i = 1
while i < len(lines):
    i += 2
    m = []
    while i < len(lines) and len(lines[i]) > 2:
        nums = re.findall(r'\d+', lines[i])
        m.append([int(n) for n in nums])
        i += 1
    maps.append(m)


for m in maps:
    tmp = []
    for seed in seeds:
        for d, s, offset in m:
            if seed >= s and seed <= s + offset - 1:
                tmp.append(d + (seed - s))
                break
        else:
            tmp.append(seed)
    seeds = tmp


print(min(seeds))
