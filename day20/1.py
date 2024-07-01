from collections import defaultdict, deque

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
for _ in range(1000):
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
            for t in targets:
                pulses.append((not all_true, t, target))

print(low)
print(high)
print(low * high)


