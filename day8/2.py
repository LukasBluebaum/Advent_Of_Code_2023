import re
from math import gcd


def lcm(a, b):
    return a*b // gcd(a, b)


def find_loop(start):
    seen = {}
    distance = 0
    d = 0
    while (start, d) not in seen:
        seen[(start, d)] = distance
        if directions[d] == 'L':
            start = graph[start][0]
        else:
            start = graph[start][1]
        distance += 1
        d = (d+1) % len(directions)

    z = [seen[x] for x in seen if x[0][-1] == 'Z']
    return z, distance - seen[(start, d)]


with open("in.txt") as file:
    lines = file.readlines()

directions = lines[0].strip()
graph = {}
starts = []
for l in lines[2:]:
    a, b, c = re.findall(r'\w+', l)
    graph[a] = (b, c)
    if a[-1] == 'A':
        starts.append(a)


tmp = []
for s in starts:
    z, d = find_loop(s)
    tmp.append(z[0])

res = 1
for t in tmp:
    res = lcm(res, t)
print(res)
