nums = [3, 4, 5, 6, 1, 2]
l, r = 0, len(nums) - 1
min_num = nums[0]
while l < r:
    mid = (l + r) // 2
    if nums[mid] > nums[r]:
        min_num = min(min_num, nums[mid])
        l = mid + 1
    else:
        r = mid
print(nums[l])
