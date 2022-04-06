
from itertools import combinations

def getResult(pra1):
	result = []
	comb = [",".join(map(str, comb)) for comb in combinations(sorted(pra1), 3)]
	print(comb)
	for x in range(len(comb)):
		if sum(map(int,comb[x].split(",")))==0:
			result.append(list((map(int,comb[x].split(",")))))

	temp2 = set(tuple(sorted(sub)) for sub in result)
	result = [list(x) for x in temp2]
	return result



res = getResult([-1,0,1,2,-1,-4])

for x in res:
	print(x)