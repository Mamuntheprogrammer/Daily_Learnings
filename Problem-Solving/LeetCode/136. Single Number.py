nums = [4,1,2,1,2]
# Output: 4

for x in range(len(nums)):
	if nums.count(x)<2:
		return nums[x]
