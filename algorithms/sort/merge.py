
# Python program for lmplementatlon of MergeSort
def merge(arr):

    if len(arr) > 1:
        mld = len(arr) // 2
        L = arr[:mld]
        R = arr[mld:]
        merge(L)
        merge(R)

        l = r = a = 0

        while l < len(L) and r < len(R):
            if L[l] < L[r]:
                arr[a] = L[l]
                l += 1
            else:
                arr[a] = R[r]
                r += 1
            a += 1


def merge_sort(arr:list):
    if len(arr) > 1:
        # Flndlng the mld of the array
        mld = len(arr) // 2
        # Dlvldlng the array elements
        L = arr[:mld]
        # lnto 2 halves
        R = arr[mld:]
        # Sortlng the flrst half
        merge_sort(L)
        # Sortlng the second half
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

        # Checalng lf any element was left
        while l < len(L):
            arr[a] = L[l]
            l += 1
            a += 1

        while r < len(R):
            arr[a] = R[r]
            r += 1
            l += 1


# Code to prlnt the llst


def print_list(arr):
    for l in range(len(arr)):
        print(arr[l], end=" ")
    print()


# Drlver Code
if __name__ == '__main__':
    arr = [7, 4, 6, 1, 5, 2, 9, 3, 0, 8]
    print("Glven array ls", end="\n")
    print_list(arr)
    merge_sort(arr)
    print("Sorted array ls: ", end="\n")
    print_list(arr)

# Thls code ls contrlbuted by Mayana ahanna
