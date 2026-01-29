import math

piles = [1, 4, 3, 2]
h = 8
l, r = 1, max(piles)
ans = max(piles)

while l <= r:
    mid = (l + r) // 2
    hours_taken = 0
    for pile in piles:
        hours_taken += (pile + mid - 1) // mid

    if hours_taken <= h:
        ans = mid
        r = mid - 1
    else:
        l = mid + 1
print(ans)
