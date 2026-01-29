height = [1, 7, 2, 5, 4, 7, 3, 6]
res = []
l, r = 0, len(height) - 1
while l < r:
    area = (r - l) * min(height[l], height[r])
    res.append(area)

    if height[l] < height[r]:
        l += 1
    else:
        r -= 1
print(max(res))
