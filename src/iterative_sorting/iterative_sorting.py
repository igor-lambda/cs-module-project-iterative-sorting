# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i+1, len(arr)):
            if arr[cur_index] > arr[j]:
                cur_index = j

        # TO-DO: swap
        # Your code here
        temp = arr[i]
        arr[i] = arr[cur_index]
        arr[cur_index] = temp 

    return arr

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    # Your code here

    return arr

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):
    # Your code here

    return arr
