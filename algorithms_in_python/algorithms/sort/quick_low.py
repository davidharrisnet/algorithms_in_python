from algorithms_in_python.utils.lists import random_int_list
import random
from copy import copy, deepcopy
# https://pyshine.com/Quicksort-algorithms-in-python/
def get_random_index(low,high):
    
    return random.randint(low,high)


def partition_low(arr, low, high):

    pivot = arr[low] # the lowest index
    i = low + 1   
   
    # partition the input
    for j in range(low+1, high):
        if arr[j] < pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    
    # place the pivot between the lower and greater elements
    arr[i-1], arr[low] = arr[low], arr[i-1]

    return i - 1

def partition_high(arr, low, high):
    pivot = arr[high]  # Choose last element as pivot
    i = low - 1        # Index of smaller element

    for j in range(low, high):
        if arr[j] <= pivot:  # If current element is smaller than or equal to pivot
            i += 1           # Increment index of smaller element
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Place pivot in its correct position
    return i + 1  # Return pivot index

def partition_random(arr, low, high):
    pi = random.randint(low,high)
    arr[pi], arr[high] =  arr[high], arr[pi]
       
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
      
    arr[i], arr[high] = arr[high], arr[i]
   
    # The array is divided into two sub-parts with the left part having all the elements smaller than the pivot and right part having elements bigger than the pivot.
    return i

def quickSortHigh(array, low, high):

   if low < high:

        # find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition_high(array, low, high)

        # recursive call on the left of pivot
        quickSortHigh(array, low, pi - 1)

        # recursive call on the right of pivot
        quickSortHigh(array, pi + 1, high)


def quickSortLow(array, low, high):

   if low < high:

        # find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition_low(array, low, high)

        # recursive call on the left of pivot
        quickSortLow(array, low, pi - 1)

        # recursive call on the right of pivot
        quickSortLow(array, pi + 1, high)

# low
def hoare_partition(arr, low, high):
    pivot = arr[low]
    i = low - 1
    j = high + 1
    while True:
        i = i + 1
        while arr[i] < pivot:
            i = i + 1
        j = j - 1
        while arr[j] > pivot:
            j = j - 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]




def quickSortRandom(array, low, high):

   if low < high:

        # find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition_random(array, low, high)

        # recursive call on the left of pivot
        quickSortRandom(array, low, pi - 1)

        # recursive call on the right of pivot
        quickSortRandom(array, pi + 1, high)
        
def quick_sort(arr, low, high):
    if low < high:
        p = hoare_partition(arr, low, high)
        quick_sort(arr, low, p-1)
        quick_sort(arr, p+1, high)


if __name__ == "__main__":

    data = [3, 8, 7, 2, 1, 0, 9,4, 6,7,8]
    print("Unsorted Array", data)    
    size = len(data)
    data2 = copy(data)
    
    quickSortHigh(data2, 0, size-1)
    print("High ", data2)
    quickSortRandom(data, 0, size-1)
    
    
    print("Random: ", data)
    