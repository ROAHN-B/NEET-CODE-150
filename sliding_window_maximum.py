nums = [-7, -8, -7, -5, -6]
k = 2
l, r = 0, k
window = []
output = []


while r <= len(nums):
    for ele in range(l, r):
        window.append(nums[ele])
    output.append(max(window))
    window.clear()
    l += 1
    r += 1
print(output)
