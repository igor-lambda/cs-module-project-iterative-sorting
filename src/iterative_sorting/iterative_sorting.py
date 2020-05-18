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
    for i in range(0, len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

    return arr

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):
    # Your code here
    count_arr = [0] * 10

    # Add count of item in arr at count_arr[item]
    for i in arr:
        count_arr[i] = count_arr[i] + 1

    # Count of next item in array is addition of next and last
    for i in range(len(arr) - 1):
        count_arr[i+1] = count_arr[i+1] + count_arr[i]
    
    new_arr = [0] * (len(arr) - 1)
    print(new_arr, 'new_arr')
    for i in arr:
        for j in count_arr:
            # print(new_arr[count_arr[i]], "new_count[count_arr[i]]")
            # new_arr[count_arr[i]] = i
            new_arr[count_arr[i] - 1 ] = i
        count_arr[i] = (count_arr[i] - 1) 
    
    print(new_arr)
    return arr

