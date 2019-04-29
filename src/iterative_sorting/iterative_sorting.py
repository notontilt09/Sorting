# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
             
        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    #### RECURSIVE
    # swaps = 0
    # for i in range(0, len(arr) - 1):
    #     if arr[i] > arr[i+1]:
    #         arr[i], arr[i+1] = arr[i+1], arr[i]
    #         swaps += 1
    # if swaps > 0:
    #     bubble_sort(arr)
    # return arr

    ## ITERATIVE SOLUTION
    for i in range(0, len(arr)):
      for j in range(0, len(arr)-1-i):
          if arr[j] > arr[j+1]:
              arr[j+1], arr[j] = arr[j], arr[j+1]
    return arr

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    if not len(arr):
        return []

    if (min(arr) < 0):
        return "Error, negative numbers not allowed in Count Sort"

    # array of counts of each item in arr initialized to 0s
    count = [0 for i in range(0, max(arr) + 1)]

    # counts of each item in arr
    for i in range(0, len(arr)):
        count[arr[i]] +=  1

    # translate count array into resulting array
    final_index = 0

    for i in range(0, len(count)):
        while (count[i] > 0):
            arr[final_index] = i
            final_index += 1
            count[i] -= 1

    return arr
