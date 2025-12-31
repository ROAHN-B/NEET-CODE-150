nums = [4, 6, 5]
target = 9
set = {}

for i, num in enumerate(nums):
    diff = target - num
    if diff in set:
        lst1 = (set[diff], i)
    set[num] = i

output = list(lst1)
print(lst1)
