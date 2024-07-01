import re
from collections import defaultdict


r, g, b = 12, 13, 14

with open('in.txt') as file:
    lines = file.readlines()

res = 0
for line in lines:
    id_ = line.split(':')
    tmp = id_[1].split(';')
    id_ = int(re.findall(r'\d+', id_[0])[0])
    counts = defaultdict(int)
    for l in tmp:
        tmp2 = re.findall(r'(\d+|blue|red|green)', l)
        for c, color in zip(tmp2[::2], tmp2[1::2]):
            counts[color] = max(counts[color], int(c))
        if counts['red'] > r or counts['green'] > g or counts['blue'] > b:
            break
    else:
        res += id_
print(res)
