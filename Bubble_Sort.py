# Python program for implementation of Bubble Sort.
import time
begin = time.time()
def bubble_Sort(arr):
	n = len(arr)

	# Traverse through all array elements
	for i in range(n-1):
		for j in range(0, n-i-1):
			if arr[j] > arr[j+1] :
				arr[j], arr[j+1] = arr[j+1], arr[j]

# main function
arr = [64, 34, 25, 12, 22, 11, 90, 78, -23, 45, -1, 0, 0]
bubble_Sort(arr)

print ("Sorted array is:")
for i in range(len(arr)):
	print ("%d" %arr[i])
end = time.time()
print(end-begin/10000)