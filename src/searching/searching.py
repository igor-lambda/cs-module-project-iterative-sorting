def linear_search(arr, target):
    # Your code here
    for index, item in enumerate(arr):
        if item == target:
            return index

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (end + start) // 2

        if arr[mid] == target: # If mid is target, just return id
            return mid

        if arr[mid] < target:  # If el at mid is less than target, it means we have to look at the right side
            start = mid + 1

        elif arr[mid] > target:  # Else, look at the left
            end = mid - 1

    return -1 

