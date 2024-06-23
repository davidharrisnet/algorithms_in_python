from algorithms_in_python.utils.lists import random_int_list
import random

def quicksort(arr, low, high):
    if low < high:       
        index = partition_high(arr,low,high)

        quicksort(arr,low, index -1)
        quicksort(arr, index + 1, high)

def get_random_index(low,high,arr):
    
    return random.randint(low,high)
   

def partition_random(arr,low,high):
    index = get_random_index(low, high,arr)
   
    arr[index], arr[high] = arr[high], arr[index]
    return partition_high(arr, low, high)


def partition_high(arr, low, high):
    
    pivot = arr[high]
    pindex = low
    
    for i in range(low, high-1):
        if arr[i] >= pivot:            
            pindex+=1
            
    return pindex + 1

def partition_high_weird(arr, low, high):

    pivot = arr[high]
    i = low - 1
    for j in range(low, high):

        if arr[j] <= pivot and i != j:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i+1]
    return i + 1


def partition_low(arr, low, high):
    pivot = arr[low]  # this will change

    i = low +1

    for j in range(low +1, high + 1): # range stops at the index before high
        if arr[j] < pivot: # ? <= ?

            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i - 1], arr[low] = arr[low], arr[i - 1]

    return i - 1

def main(arr):
    if len(arr) <= 1:
        return arr
    else:
        return quicksort(arr,0,len(arr)-1)

if __name__ == "__main__":
    a = list(range(20,0,-1))
    #a = random_int_list(0,100,40)
    a = [ 10, 8, 12, 15, 6, 3, 9, 5]
    print(a)
    main(a)
    print(a)