'''
First, we check the widest possible container starting from the first line to the last one.
 Next, we ask ourselves, how is it possible to form an even bigger container? 
 Every time we narrow the container, the width becomes smaller so the only way to get a bigger area is to find higher lines. 
 So why not just greedily shrink the container on the side that has a shorter line? 
 Every time we shrink the container, we calculate the area and save the maximum



'''
from typing import List

class Solution:
	def maxArea(self, height: List[int]) -> int:
		l,r,area = 0,len(height)-1,0

		while l<r:
			area = max(area, (r-l) * min(height[l],height[r]))
			if height[l] < height[r]:
				l += 1
			else:
				r -= 1
		return area


ob = Solution()

print(ob.maxArea([1,8,6,2,5,4,8,3,7]))