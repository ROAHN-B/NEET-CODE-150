nums = [1, 2, 3, 4, 4]
map = {}
duplicate = 0

for ele in nums:
    if ele in map:
        map[ele] += 1
    else:
        map[ele] = 1
    if map[ele] >= 2:
        duplicate = ele
        break

print(duplicate)
