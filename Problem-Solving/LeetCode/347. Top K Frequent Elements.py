'''
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

'''


from collections import Counter

nums = [4,1,-1,2,-1,2,3]
k = 2
temp = set(nums)

result = {}

for s in temp:
	result[s] = nums.count(s)

'''
One line solution 

print([x for x, y in Counter(nums).most_common(k)])

print([x[0] for x in Counter(nums).most_common(k)])

'''
print(list(sorted(result, key=result.get, reverse=True))[:2])