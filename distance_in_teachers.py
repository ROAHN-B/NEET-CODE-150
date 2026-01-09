rooms = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
t = 4
l, r = 1, len(rooms) - 1
max_dist = 0
while l <= r:
    mid = (l + r) // 2
    if ((mid + 1) * (t - 1)) + 1 <= len(rooms):
        max_dist = mid
        l = mid + 1
    else:
        r = mid - 1
print("Max dist is: \n", max_dist)
