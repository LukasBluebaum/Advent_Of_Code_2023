import re

with open("in.txt") as file:
    lines = file.readlines()

directions = lines[0].strip()
graph = {}
for l in lines[2:]:
    a, b, c = re.findall(r'\w+', l)
    graph[a] = (b, c)


start = "AAA"
distance = 0
d = 0
while start != 'ZZZ':
    if directions[d] == 'L':
        start = graph[start][0]
    else:
        start = graph[start][1]
    distance += 1
    d = (d+1) % len(directions)
print(distance)
