def isanyduplicate(nums):
	tem = set()
	for num in nums:
		if num in tem:
			return True
		tem.add(num)





print(isanyduplicate([1,2,3,1]))