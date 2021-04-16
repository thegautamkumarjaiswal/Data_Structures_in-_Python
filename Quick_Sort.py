# Python program for Implementation of Quick sort #
# import the date and time package for check the runtime #
import datetime
a = datetime.datetime.now()
# define the partition pivot element #
def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1

        while low <= high and array[low] <= pivot:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

# define the quick sort algorithm's variables #
def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)

# intialize the array #
array = [29,99,27,41,66,28,44,78,87,19,31,76,58,88, 12, 11, 13, 5, 6, 7, 22, 11, 90,78, -23, 45, -1, 0, 0]
quick_sort(array, 0, len(array) - 1)
# print the resultant array #
print(array)

b = datetime.datetime.now()
print((b-a).microseconds)