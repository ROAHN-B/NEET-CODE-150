nums = [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]
if not nums:
    print(0)
num_set = set(nums)
longest_streak = 0

for num in nums:
    if (num - 1) not in num_set:
        current_num = num
        current_streak = 1

        while (current_num + 1) in num_set:
            current_num += 1
            current_streak += 1
        longest_streak = max(longest_streak, current_streak)
print(longest_streak)
