nums = [-1, 0, 1, 2, 3]
res = []
n = len(nums)

for i in range(n):
    otp = 1
    for j in range(n):
        if j != i:
            otp *= nums[j]
    res.append(otp)
print(res)
