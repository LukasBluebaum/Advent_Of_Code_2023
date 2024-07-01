import re

with open('in.txt') as file:
    lines = file.readlines()

tmp = re.findall(r'\d+', lines[0])
tmp = [int(t) for t in tmp]
seeds = []
for a, b in zip(tmp[::2], tmp[1::2]):
    seeds.append((a, a+b-1))

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
    for a, b in seeds:
        for d, s, offset in m:
            if a >= s and b <= s + offset - 1:
                tmp.append((d + (a - s), d + (b - s)))
                break
            elif a >= s and a <= s + offset - 1:
                tmp.append((d + (a - s), d + offset - 1))
                a = s + offset
            elif b <= s + offset - 1 and b >= s:
                tmp.append((d, d + (b - s)))
                b = s - 1
            elif a < s and b > s + offset - 1:
                tmp.append((d, d + offset - 1))
                seeds.append((a, s - 1))
                a = s + offset
        else:
            tmp.append((a, b))

    seeds = tmp

print(min(seeds))
