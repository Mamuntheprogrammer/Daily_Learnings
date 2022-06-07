valueList = [["I",1],["IV",4],["V",5],["IX",9],["X",10],["XL",40],["L",50],["XC",90],["C",100],["CD",400],["D",500],["CM",900],["M",1000]]

num = 1994
output = "MCMXCIV"




result = ''
for string , value in reversed(valueList):
	if num // value:
		count = num//value
		result += (string*count)
		num = num % value

print(result)

