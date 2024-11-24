"""
[6, 4, 8, 0]
[4, 6, 8, 0] k = 1
[4, 6, 8, 0] k = 2
[0, 4, 6, 8] k = 3
"""


def insertion(arr):

    for i in range(1,len(arr)): 
        # k from  1 to the end of the array

        key = arr[i]  # select key at index k
        j = i -1      # select the previous index l
        '''
        While l is greater than or equal to 0 
            and the key is less than the the value at index l
               move arr[l] tp arr[l+1]
         '''
        while j >=0 and key < arr[j]: 
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key  # drop the key infront of the elements greater than it


if __name__ == "__main__":

    a = [6,2, 4, 3, 8, 0]
    print(a)
    insertion(a)
    print(a)

