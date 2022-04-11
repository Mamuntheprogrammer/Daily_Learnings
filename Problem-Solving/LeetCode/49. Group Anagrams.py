'''

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

'''
strs = ["eat","tea","tan","ate","nat","bat"]

resut = {}

for word in strs:
	w = "".join(sorted(word))
	if w in resut:
		resut[w].append(word)
	else:
		resut[w] = [word]

[resut[x] for x in resut]