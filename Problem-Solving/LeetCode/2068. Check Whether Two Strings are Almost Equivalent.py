word1 = "aaaa"
word2 = "cccc"

for x in range(len(word1)):
	if abs(word1.count(word1[x]) - word2.count(word2[x])) >=4:
		print("ok")

result = [ abs(word1.count(word1[x]) - word2.count(word2[x])) < 4 and word2.count(word1[x])>0 for x in range(len(word1)) ]

print(any(result))