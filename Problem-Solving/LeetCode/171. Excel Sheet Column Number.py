
txt = "AB"

result = 0

for x in txt:
	d = ord(x)-ord("A")+1
	result = result * 26 + d




print(result)