


ans = []
security = [4,3,2,1]

time = 1

increasing = [0]*len(security)
decreasing = [0]*len(security)



for x,y in zip(security,security[1:]):
	if x>=y:
		increasing.append(increasing[-1]+1)




security2 = security[::-1]


for x,y in zip(security,security2[1:]):
	if x<=y:
		decreasing.append(decreasing[-1]+1)



for x in range(len(security)):
	if increasing[x]>=time and decreasing[x]>=time:
		ans.append(x)

# print(security)
# print(ans)
print(decreasing)
print(increasing)



# class Solution:
#     def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
# 		# for convenience, use n
# 		n = len(security)
		
# 		# prepare non-increasing prefix array
# 		# store consecutivy non-increasing length at each index i
# 		# otherwise, the length of index i (for non-increasing property) is 1
# 		noninc = [0 for _ in range(n)]
# 		noninc[0] = 1
# 		for i in range(1, n):
# 			if security[i] <= security[i-1]:
# 				noninc[i] = noninc[i-1] + 1
# 			else:
# 				noninc[i] = 1

# 		# do the similar job for non-decreasing
# 		nondec = [0 for _ in range(n)]
# 		nondec[0] = 1
# 		for i in range(1, n):
# 			if security[i] >= security[i-1]:
# 				nondec[i] = nondec[i-1] + 1
# 			else:
# 				nondec[i] = 1

# 		res = []
# 		for i in range(time, n-time):
# 			if noninc[i] - noninc[i-time] == time and nondec[i+time] - nondec[i] == time:
# 				res.append(i)

# 		return res