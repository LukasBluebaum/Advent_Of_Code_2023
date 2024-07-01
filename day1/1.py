import re
from functools import partial

with open('in.txt') as f:
    input_ = f.readlines()

digits = {'one': '1','two': '2','three': '3','four': '4','five': '5',
          'six': '6','seven': '7','eight': '8','nine': '9'}

check = lambda a: a if len(a) == 1 else digits[a]
l = list(digits.values()) + list(digits.keys())

find_min = lambda line, a: c if (c := line.find(a)) != -1 else float('inf')
find_max = lambda line, a: line.rfind(a)
res = ((min(l, key=partial(find_min, line)), max(l, key=partial(find_max, line)))
       for line in input_)
print(sum(int(check(a) + check(b)) for a, b in res))

