from collections import defaultdict
from itertools import product


def dfs(flows, current, ranges):
    if current == 'A':
        t = 1
        for r in ranges:
            a, b = ranges[r]
            t *= b-a+1
        return t
    elif current == 'R':
        return 0

    count = 0
    for rule, target in flows[current][:-1]:
        c = rule[0]
        num = int(rule[2:])
        new_ranges = dict(**ranges)
        a, b = new_ranges[c]

        if rule[1] == '>':
            tmp_a = max(a, num+1)
            if tmp_a <= b:
                new_ranges[c] = (tmp_a, b)
                count += dfs(flows, target, new_ranges)
                ranges[c] = (a, tmp_a-1)
        else:
            tmp_b = min(b, num-1)
            if a <= tmp_b:
                new_ranges[c] = (a, tmp_b)
                count += dfs(flows, target, new_ranges)
                ranges[c] = (tmp_b+1, b)

    count += dfs(flows, flows[current][-1][0], ranges)
    return count


with open("in.txt") as file:
    lines = file.read().strip()

w, _ = lines.split("\n\n")
w = w.split("\n")

workflows = {}
for flow in w:
    name, rules = flow.split("{")
    rules = rules[:-1].split(",")
    workflows[name] = [r.split(":") for r in rules]

ranges = {'a': (1, 4000), 'x':(1, 4000), 'm': (1, 4000), 's': (1, 4000)}
print(dfs(workflows, "in", ranges))

