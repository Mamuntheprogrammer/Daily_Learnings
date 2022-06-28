# work only with sorted array
# Implementation Iterative way . (another recursive way)

def binary_search(arr,leftIndex,rightIndex,x):
	while leftIndex <= rightIndex:
		mid = (leftIndex + rightIndex)//2
		if arr[mid]==x:
			return arr[mid]
		elif arr[mid] < x:
			leftIndex = mid + 1

		else:
			rightIndex = mid -1 
	return -1




arr = [3, 4, 5, 6, 7, 8, 9]
x = 3

print(binary_search(arr,0,len(arr)-1,x))


# time complexity = log n

# space complexity = O(1)