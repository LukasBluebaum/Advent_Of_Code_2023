import re
import math


with open("in.txt") as file:
    lines = file.readlines()

times = [int(a) for a in re.findall(r'\d+', lines[0])]
distances = [int(a) for a in re.findall(r'\d+', lines[1])]

counts = [0] * len(times)
for i in range(len(times)):
    for t in range(times[i]):
        if (times[i] - t) * t > distances[i]:
            counts[i] += 1
print(math.prod(counts))
