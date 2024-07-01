from functools import cmp_to_key
from collections import Counter

cards = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
cards = {c: idx for idx, c in enumerate(cards)}

def compare_cards(a, b):
    for aa, bb in zip(a, b):
        if cards[aa] > cards[bb]:
            return -1
        elif cards[aa] < cards[bb]:
            return 1
    return 0

def check(a, b, aa, bb):
    if aa and bb:
        return compare_cards(a, b)
    elif aa:
        return 1
    elif bb:
        return -1
    else:
        return 2

def fix_joker(a):
    aa = Counter(a)
    j = aa['J']
    if j != 5 and j != 0:
        c = max(aa.keys(), key=lambda a: (aa[a] if a != 'J' else float('-inf')))
        aa['J'] = 0
        aa[c] += j
    return aa

def compare(a, b):
    a = a[0]
    b = b[0]
    if a == b:
        return 0
    checks = [lambda a: 2 in a.values(),
              lambda a: Counter(a.values())[2] > 1,
              lambda a: 3 in a.values(),
              lambda a: 3 in a.values() and 2 in a.values(),
              lambda a: 4 in a.values(),
              lambda a: 5 in a.values(),
    ]

    aa = fix_joker(a)
    bb = fix_joker(b)
    for i in range(5, -1, -1):
        tmp = check(a, b, checks[i](aa), checks[i](bb))
        if tmp < 2:
            return tmp
    return compare_cards(a, b)


with open("in.txt") as file:
    lines = file.readlines()


hands = []
ranks= []
for idx, line in enumerate(lines):
    a, b = line.strip().split(" ")
    hands.append(a)
    ranks.append(int(b))


ranks = [b for a, b in sorted(zip(hands, ranks), key=cmp_to_key(compare))]
print(sum((idx+1) * r for idx, r in enumerate(ranks)))
