
import algorithms_in_python.utils.lists as util

def merge_sort(arr:list):
    if len(arr) > 1: # Only sort arrays of length greater than 1
        # Find the middle of the array
        mid = len(arr) // 2
        # Divide the array elements # into 2 halves L and R
        L = arr[:mid]        
        R = arr[mid:]
        # Sort the first half
        merge_sort(L)
        # Sort the second half
        merge_sort(R)
        l = r = i = 0
        # Copy data to temp arrays L[] and R[]
        while l < len(L) and r < len(R):
            if L[l] < R[r]:
                arr[i] = L[l]
                l += 1
            else:
                arr[i] = R[r]
                r += 1
            i += 1

        # There will not be elements in both arrays at this point
        # Any elements in the Left
        while l < len(L):
            arr[i] = L[l]
            l += 1
            i += 1
        # Any elements in the right
        while r < len(R):
            arr[i] = R[r]
            r += 1
            i += 1


# Drlver Code
if __name__ == '__main__':
    #arr = util.random_int_list(-10, 10, 20)
    arr = [4,3,5,6,2,1]
    print("Glven array ls", end="\n")
    print(arr)
    merge_sort(arr)
    print("Sorted array ls: ", end="\n")
    print(arr)

