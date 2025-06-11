from algorithms_in_python.utils.lists import getlist, random_list
import random

# https://pyshine.com/Quicksort-algorithms-in-python/


# low
def parition_random(arr, low, high):
    # pick a random pivot
    pivot_index = random.randint(low,high)
    pivot = arr[pivot_index]

    # switch random index with low
    arr[low], arr[pivot_index] = arr[pivot_index], arr[low]

    i = low
    j = high
    while True:
        # increase i while arr[i] < pivot       
        while arr[i] < pivot:
            i = i + 1
        # decrease j while arr[j] > pivot       
        while arr[j] > pivot:
            j = j - 1
        
        if i >= j:
            return j # the pivot
        # switch the lower arr[i] with higher arr[j]
        arr[i], arr[j] = arr[j], arr[i]
        
        i+=1
        j-=1

def quick(arr, low, high):
    if low < high:
        p = parition_random(arr, low, high)
        quick(arr, low, p)
        quick(arr, p+1, high)

def quick_sort(arr):
    quick(arr, 0, len(arr)-1)
    return arr
    

if __name__ == "__main__":

    #data = getlist(200000)
    data = random_list(0,10000,10000)
    
    print("Unsorted Array", data)       
    quick_sort(data)
    print("Sorted numbers: ", data)
    in_order = [ data[i +1] >= data[i] for i in range(0,len(data)-1)]
    print(all(in_order))
