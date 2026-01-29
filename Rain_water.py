height = [4, 2, 0, 3, 2, 5]
n = len(height)
left_max = [0] * n
right_max = [0] * n
res = 0

left_max[0] = height[0]
for i in range(n):
    left_max[i] = max(height[i], left_max[i - 1])

right_max[n - 1] = height[n - 1]
for i in range(n - 2, -1, -1):
    right_max[i] = max(height[i], right_max[i + 1])

for i in range(1, n):
    water_amount = min(left_max[i], right_max[i]) - height[i]
    res += water_amount
print(res)
