'''
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

# '''

nums = [1,2,3,4]
res = []
prod = 1
for a in nums:
    res.append(prod)
    prod *= a

prod = 1
for i in range(len(nums)-1, -1, -1):
    res[i] *= prod
    prod *= nums[i]

print(res)