# # print(chr(65,90))

# result = chr(ord('A') + (1600 - 1) % 26) + ''

# print(result)


# Input: columnNumber = 28
# Output: "AB"


columnNumber = 28

result = ''

while columnNumber>0:
	
	result = chr(ord('A')+(columnNumber-1)%26 )+ result

	columnNumber = (columnNumber-1) // 26

print(result)