# Implementation of Binary Search #
print('hello world')
print(' ')

# Define the Binary search variables #
def binary_Search(array, start, end, x):
    if end >= start:    # Alot the mid value #
        mid = (start + end) // 2

        if array[mid] == x:     # Array pointer equal to mid value #
            return mid
        elif array[mid] > x:    # Array value greater than x #
            return binary_Search(array, start, mid - 1, x)
        else:       # else less than x #
            return binary_Search(array, mid + 1, end, x)

    else:
        return -1
# define array #
arr = [2, 10, 20, 40, 50, 60]
x = 10
# main function #
result = binary_Search(arr, 0, len(arr)-1, x)

# result statment #
if result != -1:
    print("Element is present at %d" % result)
else:
    print("Element is not present.")


