nums1 = []
nums2 = [1]

m=len(nums1)
n=len(nums2)
nums1.sort(reverse = False, key=None)

for i in nums2 :
    if i==0:
        nums2.remove(i)
        n=n-1
    else:
        pass


for i in nums1 :
    if i==0:
        nums1.remove(i)
        m=m-1
    else:
        pass





nums1=nums1+nums2

i=0
for i in nums1:
    if i==0:
        nums1.remove(i)
        m=m-1
    else:
        pass

print(nums1)
print("m:",m)
print("n:", n)
    





