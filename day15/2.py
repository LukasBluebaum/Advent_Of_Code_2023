with open("in.txt") as file:
    lines = file.read().strip()

nums = lines.split(",")

m = [[] for _ in range(256)]

for n in nums:
    t = 0
    for i in range(len(n)):
        if n[i] == "=" or n[i] == '-':
            break
        t = ((t + ord(n[i])) * 17) % 256

    if n[i] == '-':
        for idx, lense in enumerate(m[t]):
            if lense[0] == n[:i]:
                del m[t][idx]
                break
    else:
        for idx, lense in enumerate(m[t]):
            if lense[0] == n[:i]:
                m[t][idx] = (n[:i], n[i+1])
                break
        else:
            m[t].append((n[:i], n[i+1]))

res = 0
for idx, box in enumerate(m):
    for idx2, lense in enumerate(m[idx]):
        res += (idx+1) * (idx2+1) * int(lense[1])
print(res)

