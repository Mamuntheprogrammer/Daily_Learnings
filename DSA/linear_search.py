
def linear_Search(arr,arr_size,y):
	'''
	x = what to find in the array
	'''
	for x in range(0,arr_size):
		if arr[x] == y :
			return arr[x]
	return -1

arr = [1,2,3,4,8,9,1,2,5,1]

print(linear_Search(arr,len(arr),2))


# Time complexity : O(n)
# Space complexity : O(1)