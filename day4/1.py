import re

with open('in.txt') as file:
    lines = file.readlines()

cards = [1] * len(lines)
res1 = 0
for idx, line in enumerate(lines):
    winning, own = line.split(':')[1].split('|')
    winning = re.findall(r'\d+', winning)
    own = re.findall(r'\d+', own)
    matches = len(set(own) & set(winning))
    if matches > 0:
        res1 += 2**(matches-1)
    for i in range(idx+1, min(idx+1+matches, len(lines))):
        cards[i] += cards[idx]

print(res1)
print(sum(cards))
