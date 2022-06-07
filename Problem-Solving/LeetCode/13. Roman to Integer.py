hasgMap ={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

result2 = 0

for i in range(len(output)):
	if i+1 < len(output) and hasgMap[output[i]]<hasgMap[output[i+1]]:
		result2 -= hasgMap[output[i]]
	else:
		result2 += hasgMap[output[i]]
print("Result2 : ",result2)