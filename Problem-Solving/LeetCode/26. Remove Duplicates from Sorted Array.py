nums=[1,1,2]

# s = set(nums)

# nums[:len(s)] = sorted(s)

# print(nums)

# k = len(s)

# print(k)

l = 1

for x in range(1,len(nums)):
	if nums[x] != nums[x-1]:
		nums[l]=nums[x]
		l+=1