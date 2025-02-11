from algorithms_in_python.algorithms.sort import quick_random
from algorithms_in_python.utils.lists import getlist, random_list
import random


    

def recursive_binary_search(arr,low, high, target):
    if low <= high:
        mid = (high + low) // 2
       
        if target == arr[mid]:
            return mid
        elif  arr[mid] > target:
            return recursive_binary_search(arr, low, mid -1, target)
        else: 
            return recursive_binary_search(arr, mid+1, high, target)
    else:
        return -1

    

def iterative_binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:            
        mid = (high + low) // 2
        if target > arr[mid]:
            low = mid + 1
        elif target < arr[mid]:
            high = mid - 1
        else:
            return mid
    return -1
    

def binary_search(arr, target):
    ri = recursive_binary_search(arr,0, len(arr)-1, target)
    li = iterative_binary_search(arr, target)
    assert(ri == li)


"""
length = 10000
arr = random_list(0,10000,10000)

arr = quick_random.quick_sort(arr)
index = random.randint(0,length)
target = arr[index]

binary_search(arr, target)
"""

arr = [ 1,3,5]

i = bsearch(arr,3)
print(i)
i = bsearch(arr,5)
print(i)
i = bsearch(arr,5)
print(i)


