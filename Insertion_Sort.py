# Python program for implementation of Insertion Sort.
def insertion_Sort(arr):

	# Traverse through 1 to len(arr).
	for i in range(1, len(arr)):
		key = arr[i]
		j = i-1
		while j >= 0 and key < arr[j] :
				arr[j + 1] = arr[j]
				j -= 1
		arr[j + 1] = key

# Main function.
arr = [12, 11, 13, 5, 6, 7, 23, 1, 2, 0, -1, -12]
insertion_Sort(arr)
for i in range(len(arr)):
	print ("% d" % arr[i])
