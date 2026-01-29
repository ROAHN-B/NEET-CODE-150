class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        a=nums1+nums2
        a.sort(reverse=False, key=None)
        n=len(a)
        if n%2==0:
            res=(a[n//2-1]+a[n//2])/2
        else:
            res = (a[n//2])
        return(float(res))
        

c1=Solution()
c1.findMedianSortedArrays([1,2],[3,4])