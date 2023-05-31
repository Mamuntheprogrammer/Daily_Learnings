def isAnagram(s,t):
	if len(s) != len(t):
		return False

	scount , tcount = {},{}


	for i in range(len(s)):
		scount[s[i]] = 1 + scount.get(s[i],0)
		tcount[t[i]] = 1 + tcount.get(t[i],0)

	return scount == tcount






s ,t = "anagram", "nxgaram"

print(isAnagram(s,t))