"""

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


"""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    	d = {}
    	for x in range(len(nums)):
    		if (target - nums[x]) in d:
    			return [d[target-nums[x]],x]
    		d[nums[x]] = x


solve = Solution()

print(solve.twoSum([2,7,11,15],9))