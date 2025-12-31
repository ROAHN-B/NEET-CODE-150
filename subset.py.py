nums=[1,2,2]

nums.sort()
last_ele=[[]]
subsets=[]

for i in range(len(nums)):
    curr_subset=[]

    if i>0 and nums[i]==nums[i-1]:
        for curr_set in subsets:
            curr_subset.append([nums[i]]+curr_set)
    else:
        for curr_set in last_ele:
            curr_subset.append([nums[i]]+curr_set)
    subsets=curr_subset
    last_ele+=curr_subset
print(last_ele)