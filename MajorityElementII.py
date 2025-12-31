nums = [1]
n=len(nums)
times= n//3

freq={}

for ele in nums:
    freq[ele]=freq.get(ele,0)+1

output = [ele for ele , count in freq.items() if count>times]

print(output)