strs = ["eat","tea","tan","ate","nat","bat"]



from collections import defaultdict


#  if key not found it will return empty list as default value thats why defaultdict used

res = defaultdict(list)

for s in strs:
	temp = [0]*26

	for x in s:
		temp[ord(x)-ord("a")] +=1

	# here tuple is used because , list can't be dictionary's key because it is mutable
	res[tuple(temp)].append(s)


print(res)



