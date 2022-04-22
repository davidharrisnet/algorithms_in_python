"""
    /* low  --> Starting index,  high  --> Ending index */
    quickSort(arr[], low, high)
    {
        if (low < high)
        {
            /* pi is partitioning index, arr[pi] is now
               at right place */
            pi = partition(arr, low, high);

            quickSort(arr, low, pi - 1);  // Before pi
            quickSort(arr, pi + 1, high); // After pi
        }
    }

"""

def quick(arr, low, high):
    if low < high:
        pivot_index = partition(arr,low,high)

        quick(arr,low, pivot_index -1)
        quick(arr, pivot_index+1, high)
"""
/* This function takes last element as pivot, places
   the pivot element at its correct position in sorted
    array, and places all smaller (smaller than pivot)
   to left of pivot and all greater elements to right
   of pivot */
partition (arr[], low, high)
{
    // pivot (Element to be placed at right position)
    pivot = arr[high];  
 
    i = (low - 1)  // Index of smaller element and indicates the 
                   // right position of pivot found so far

    for (j = low; j <= high- 1; j++)
    {
        // If current element is smaller than the pivot
        if (arr[j] < pivot)
        {
            i++;    // increment index of smaller element
            swap arr[i] and arr[j]
        }
    }
    swap arr[i + 1] and arr[high])
    return (i + 1)
}
"""



def partition(arr, low, high):
    pivot = arr[high]  # this will change

    i = low -1

    for j in range(low, high-1):
        if arr[j] < pivot:
            i += 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

    temp = arr[i + 1]
    arr[i + 1] = arr[high]
    arr[high] = temp
    return i + 1

def quickSort(arr):
    return quick(arr,0,len(arr)-1)

if __name__ == "__main__":
    a = [7, 4, 6, 1, 5, 2, 9, 3, 0, 8]
    #a = [2,1]
    print(a)
    quickSort(a)
    print(a)