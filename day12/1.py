
def check(i, j, current, chars, nums, dp):
    if i >= len(chars) and j >= len(nums):
        return int(current == 0)
    elif j >= len(nums):
        return int(all(chars[k] != '#' for k in range(i, len(chars))))
    elif i >= len(chars):
        return int(j == len(nums) - 1 and current == nums[j])

    if (i, j, current) in dp:
        return dp[(i, j, current)]

    count = 0
    if current == nums[j] and chars[i] != '#':
        count = check(i+1, j+1, 0, chars, nums, dp)
    elif chars[i] == '#' and current != nums[j]:
        count = check(i+1, j, current+1, chars, nums, dp)
    elif chars[i] == '.' and current == 0:
        count = check(i+1, j, 0, chars, nums, dp)
    elif chars[i] == '?':
        count = check(i+1, j, current+1, chars, nums, dp)
        if current == 0:
            count += check(i+1, j, 0, chars, nums, dp)
    dp[(i, j, current)] = count
    return count

with open("in.txt") as file:
    lines = file.readlines()

lines = [l.strip() for l in lines]

chars = []
nums = []
for line in lines:
    a, b = line.split(" ")
    chars.append(a)
    nums.append([int(n) for n in b.split(",")])

res = 0
for c, n in zip(chars, nums):
    tmp = check(0, 0, 0, c, n, {})
    res += tmp
print(res)
