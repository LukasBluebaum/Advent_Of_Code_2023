from collections import defaultdict
from math import prod
import re

with open("in.txt") as file:
    lines = file.readlines()
lines = [line.strip() for line in lines]


def find_symbol(lines, i, j, y, num):
    def helper(i):
        for k in range(j-1, y+2):
            if k > 0 and k < len(lines[0]) and lines[i][k] != '.' and not lines[i][k].isnumeric():
                return True, (i, k)
        return False, None

    if j > 0 and lines[i][j-1] != '.':
        return True, (i, j-1)
    if y < len(lines[0]) - 1 and lines[i][y+1] != '.':
        return True, (i, y+1)
    # Could actually be wrong if the '*' appears in the second if and another symbol appears in
    # the first if
    if i > 0:
        found, x = helper(i-1)
        if found:
            return found, x
    if i < len(lines) - 1:
        found, x = helper(i+1)
        if found:
            return found, x
    return False, (i, j)


gears = defaultdict(list)
res = 0
for i in range(len(lines)):
    for match_ in re.finditer(r'\d+', lines[i]):
        j, y = match_.span()
        num = int(match_.group())
        found, (ii, jj) = find_symbol(lines, i, j, y-1, num)
        if found:
            res += num
        if lines[ii][jj] == '*':
            gears[(ii, jj)].append(num)

print(res)
print(sum(prod(gears[x]) for x in gears if len(gears[x]) == 2))




