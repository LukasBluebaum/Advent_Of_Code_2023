import re
from collections import defaultdict

with open('in.txt') as file:
    lines = file.readlines()

res = 0
for line in lines:
    tmp = line.split(':')[1].split(';')
    counts = defaultdict(int)
    for l in tmp:
        tmp2 = re.findall(r'(\d+|blue|red|green)', l)
        for c, color in zip(tmp2[::2], tmp2[1::2]):
            counts[color] = max(counts[color], int(c))
    res += counts['red'] * counts['blue'] * counts['green']
print(res)
