import re
import math

with open("in.txt") as file:
    lines = file.readlines()

time = int(''.join(re.findall(r'\d+', lines[0])))
distance = int(''.join(re.findall(r'\d+', lines[1])))

l = 0
r = time
while l <= r:
    mid = l + (r - l) // 2
    if (time - mid) * mid > distance:
        r = mid - 1
    else:
        l = mid + 1

start = r + 1

l = 0
r = time
while l <= r:
    mid = l + (r - l) // 2
    if (time - mid) * mid > distance:
        l = mid + 1
    else:
        r = mid - 1

print(l - start)
