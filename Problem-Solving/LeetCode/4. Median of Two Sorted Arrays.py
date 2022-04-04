'''
Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

'''



from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        temp = sorted(nums1+nums2)

        if len(temp)%2==0:
            return ((temp[len(temp)//2]+temp[(len(temp)//2)-1])/2) # -1 used bcoz of list index start from 0
        return temp[(len(temp)//2)]

result = Solution()
print(result.findMedianSortedArrays([1,2],[3,4]))