with open("test.txt") as file:
    lines = file.read().strip()

nums = lines.split(",")

res = 0
for n in nums:
    t = 0
    for c in n:
        t = ((t + ord(c)) * 17) % 256
    print(t)
    res += t

print(res)

