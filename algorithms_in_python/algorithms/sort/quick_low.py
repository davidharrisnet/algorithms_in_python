from algorithms_in_python.utils.lists import random_int_list
import random
from copy import copy, deepcopy

# https://pyshine.com/Quicksort-algorithms-in-python/

def get_random_index(low,high):    
    return random.randint(low,high)

def partition_low(arr, low, high):

    pivot = arr[low] # the lowest index
    i = low - 1
   
    j = high +1
    while True:
        i += 1
        while arr[i] < pivot:
            i+=1
        j -= 1
        while arr[j] > pivot:            
            j-=1
            
        if i >= j:                       
            return j
                                           
        arr[i], arr[j] = arr[j], arr[i]


def partition_high(arr, low, high):
    pivot = arr[high]  # Choose last element as pivot
    i = low - 1        # Index of smaller element

    for j in range(low, high):
        if arr[j] <= pivot:  # If current element is smaller than or equal to pivot
            i += 1           # Increment index of smaller element
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Place pivot in its correct position
    return i + 1  # Return pivot index


def quickSortHigh(array, low, high):

   if low < high:

        # find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition_high(array, low, high)

        # recursive call on the left of pivot
        quickSortHigh(array, low, pi-1)

        # recursive call on the right of pivot
        quickSortHigh(array, pi + 1, high)


def quickSortLow(array, low, high):

   if low < high:

        # find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition_low(array, low, high)

        # recursive call on the left of pivot
        quickSortLow(array, low, pi)

        # recursive call on the right of pivot
        quickSortLow(array, pi + 1, high)



if __name__ == "__main__":

    data = [2, 9, 6, 4, 3, 7] 
    quickSortHigh(data, 0, len(data)-1)
    print("High ", data)
   
    data = [5,2, 9, 6, 4, 3, 7] 
    quickSortLow(data, 0, len(data)-1)
    print("Low ", data)
   
    