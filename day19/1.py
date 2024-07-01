
def find(flows, part):
    current = 'in'
    while True:
        for rule, target in flows[current][:-1]:
            if ">" in rule and part[rule[0]] > int(rule[2:]):
                current = target
                break
            elif "<" in rule and part[rule[0]] < int(rule[2:]):
                current = target
                break
        else:
            current = flows[current][-1][0]
        if current == "A":
            return True
        elif current == "R":
            return False


with open("in.txt") as file:
    lines = file.read().strip()

w, p = lines.split("\n\n")
w = w.split("\n")
p = p.split("\n")

workflows = {}
for flow in w:
    name, rules = flow.split("{")
    rules = rules[:-1].split(",")
    workflows[name] = [r.split(":") for r in rules]

parts = []
for part in p:
    nums = part[1:-1].split(",")
    parts.append({n.split("=")[0]: int(n.split("=")[1]) for n in nums})


res = 0
for part in parts:
    if find(workflows, part):
        res += sum(part.values())
print(res)
