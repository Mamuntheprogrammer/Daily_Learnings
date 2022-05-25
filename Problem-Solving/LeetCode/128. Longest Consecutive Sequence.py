nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
set_nums = sorted(set(nums))

maxc = 0
for x in set_nums:
	if x-1 not in set_nums:
		count = 0
	count+=1
	if maxc<count:
		maxc=count

print(maxc)