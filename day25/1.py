from collections import defaultdict
import re
import random
from copy import deepcopy

class DSU:

    def __init__(self, n):
        self.parents = {n: n for n in nodes}
        self.rank = {n: 0 for n in nodes}

    def find(self, x):
        while x != self.parents[x]:
            self.parents[x] = self.parents[self.parents[x]]
            x = self.parents[x]
        return x

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return

        if self.rank[x] > self.rank[y]:
            self.parents[y] = x
        elif self.rank[x] < self.rank[y]:
            self.parents[x] = y
        else:
            self.parents[x] = y
            self.rank[x] += 1


with open("in.txt") as file:
    lines = file.readlines()

nodes = set()
edges = []
for line in lines:
    comps = re.findall(r'\w+', line)
    nodes.add(comps[0])
    for j in range(1, len(comps)):
        edges.append((comps[0], comps[j]))
        nodes.add(comps[j])


while True:
    graph = DSU(nodes)
    n = len(nodes)
    while n > 2:
        edge = random.choice(edges)
        c1, c2 = graph.find(edge[0]), graph.find(edge[1])
        if c1 == c2:
            continue
        n -= 1
        graph.union(edge[0], edge[1])

    count = 0
    for a, b in edges:
        c1, c2 = graph.find(a), graph.find(b)
        if c1 != c2:
            count += 1
    if count == 3:
        break


comps = defaultdict(int)
for n in nodes:
    comps[graph.find(n)] += 1

sizes = list(comps.values())
print(sizes[0] * sizes[1])
