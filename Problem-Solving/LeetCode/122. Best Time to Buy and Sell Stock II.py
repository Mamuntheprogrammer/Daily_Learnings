
# Technique : Slide Window (TWO POINTER)
prices = [7,1,5,3,6,4]

r,l = 1,0 

result = 0 

while r < len(prices):
	if prices[l]<prices[r]:
		profit = prices[r]-prices[l]
		result += profit 
	else:
		l = r
	r+=1

print(result)