nums = [2,7,11,15]
target = 9

temp = {}

for i,v in enumerate(nums):
	trg = target-v
	if trg in temp:
		print(i,temp[trg])
	temp[v]=i