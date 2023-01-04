class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        # nums = [0,2,1,5,3,4]
        return [nums[nums[x]] for x in range(len(nums))]
        