
def find(line):
    diffs = []
    while not all(l == 0 for l in line):
        diffs.append(line)
        line = [b - a for a, b in zip(line, line[1::])]

    current_left = 0
    current_right = 0
    for i in range(len(diffs)-1, -1, -1):
        current_right = current_right + diffs[i][-1]
        current_left = diffs[i][0] - current_left
    return current_left, current_right


with open("in.txt") as file:
    lines = file.readlines()

lines = [[int(a) for a in line.strip().split(" ")] for line in lines]

left = 0
right = 0
for line in lines:
    l, r = find(line)
    left += l
    right += r
print(left, right)
