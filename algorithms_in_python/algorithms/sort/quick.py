from algorithms_in_python.utils.lists import random_int_list
import random
import sys
print(sys.path)
def quicksort(arr, low, high):
    if low < high:
        pivot = get_random_pivot(low, high,arr)
        index = partition_random(arr,low,high,pivot)

        quicksort(arr,low, index -1)
        quicksort(arr, index+1, high)

def get_random_pivot(low,high,arr):
    return arr[random.randint(low,high)]

def partition_random(arr,low,high,pivot):
    while low < high:
        while arr[low] < pivot:
            low+= 1
        while arr[high] > pivot:
            high -= 1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            low+=1
            high-=1
    return low



def partition_high(arr, low, high):

    pivot = arr[high]
    i = low - 1
    for j in range(low, high):

        if arr[j] <= pivot:
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
    a = random_int_list(0,20,10)

    print(a)
    main(a)
    print(a)