nums=[3,2,3]

counts = {}
n = len(nums)
for num in nums:
    counts[num] = counts.get(num, 0) + 1
    if counts[num] > n // 2:
        print( num)