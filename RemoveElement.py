class Solution(object):
    def removeElement(self, nums, val):
        i=0
        for ele in range(len(nums)):
            if nums[ele] !=val:
                nums[i]=nums[ele]
                i=i+1
        return (i)

s1=Solution()
s1.removeElement([2], 3)