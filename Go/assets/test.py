nums1 = [1,3]
nums2 = [2]

temp = sorted(nums1+nums2)
if len(temp)%2==0:
    print((temp[len(temp)//2]+temp[(len(temp)//2)+1]/2))
else:
	print(temp[(len(temp)//2)])


# return 
