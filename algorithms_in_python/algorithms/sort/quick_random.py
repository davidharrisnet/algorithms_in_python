from algorithms_in_python.utils.lists import getlist, random_int_list
import random

# https://pyshine.com/Quicksort-algorithms-in-python/


# low
def parition_random(arr, low, high):
    pivot_index = random.randint(low,high)
    pivot = arr[pivot_index]

    # switch random index with low
    arr[low], arr[pivot_index] = arr[pivot_index], arr[low]

    i = low - 1
    j = high + 1
    while True:
        # increase i while arr[i] < pivot
        i = i + 1
        while arr[i] < pivot:
            i = i + 1
        # decrease j while arr[j] > pivot
        j = j - 1
        while arr[j] > pivot:
            j = j - 1
        
        if i >= j:
            return j # the pivot
        # switch the lower arr[i] with higher arr[j]
        arr[i], arr[j] = arr[j], arr[i]

def quick_sort(arr, low, high):
    if low < high:
        p = parition_random(arr, low, high)
        quick_sort(arr, low, p)
        quick_sort(arr, p+1, high)


if __name__ == "__main__":

    data = getlist(20)
    
    print("Unsorted Array", data)
    
    size = len(data)

    quick_sort(data, 0, size-1)
    print("Sorted numbers: ", data)
    