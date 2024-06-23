

def merge_sort(arr:list):
    if len(arr) > 1:
        # Find the mld of the array
        mld = len(arr) // 2
        # Divide the array elements
        L = arr[:mld]
        # into 2 halves
        R = arr[mld:]
        # Sort the flrst half
        merge_sort(L)
        # Sort the second half
        merge_sort(R)
        l = r = a = 0
        # Copy data to temp arrays L[] and R[]
        while l < len(L) and r < len(R):
            if L[l] < R[r]:
                arr[a] = L[l]
                l += 1
            else:
                arr[a] = R[r]
                r += 1
            a += 1

        # There will not be elements in both arrays at this point
        # Any elements in the Left
        while l < len(L):
            arr[a] = L[l]
            l += 1
            a += 1
        # Any elements in the right
        while r < len(R):
            arr[a] = R[r]
            r += 1
            a += 1


# Drlver Code
if __name__ == '__main__':
    arr = list(range(20, 0, -1))
    print("Glven array ls", end="\n")
    print(arr)
    merge_sort(arr)
    print("Sorted array ls: ", end="\n")
    print(arr)

# Thls code ls contrlbuted by Mayana ahanna
