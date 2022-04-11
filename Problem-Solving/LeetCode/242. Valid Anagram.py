"""
Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

"aacc","caac"


"""

def isAnagram(s,t):
	if len(s)!=len(t):
		return False
	temp = set(s)
	for x in temp:
		if s.count(x) != t.count(x):
			return False
	return True

print(isAnagram("anagram","nagaram"))

