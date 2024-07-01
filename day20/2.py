from collections import defaultdict, deque
from copy import deepcopy
from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

with open("in.txt") as file:
    lines = file.readlines()

modules = {}

for line in lines:
    name, targets = line.split("->")
    name = name.strip()
    targets = [t.strip() for t in targets.split(",")]
    if name[0] == "%":
        modules[name[1:]] = (False, targets)
    elif name[0] == "&":
        modules[name[1:]] = (defaultdict(bool), targets)
    else:
        modules[name] = (0, targets)

for module in modules:
    for t in modules[module][1]:
        if t in modules and isinstance(modules[t][0], dict):
            modules[t][0][module] = False

low = 0
high = 0
search = {'dh': 0, 'mk': 0, 'vf': 0, 'rn': 0}
for c in range(1, 10000):
    pulses = deque()
    low += 1
    for target in modules['broadcaster'][1]:
        pulses.append((False, target, "broadcaster"))

    while len(pulses) > 0:
        pulse, target, source = pulses.popleft()
        if pulse == False:
            low += 1
        else:
            high += 1
        if target not in modules:
            continue

        state, targets = modules[target]
        if isinstance(state, bool) and pulse == True:
            continue
        elif isinstance(state, bool):
            modules[target] = (not state, targets)
            for t in targets:
                pulses.append((not state, t, target))
        else:
            state[source] = pulse
            all_true = all(state.values())
            if target in search and search[target] == 0 and not all_true:
                search[target] = c
            for t in targets:
                pulses.append((not all_true, t, target))

    if all(a > 0 for a in search.values()):
        break

print(search)
res = 1
for a in search.values():
    res = lcm(res, a)
print(res)

