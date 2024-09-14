"""
[6, 4, 8, 0]
[4, 6, 8, 0] k = 1
[4, 6, 8, 0] k = 2
[0, 4, 6, 8] k = 3
"""


def insertion(arr):

    for k in range(1,len(arr)):
        print(arr)
        key = arr[k]  # the key from 1 to the end
        l = k -1      # the element before key
        '''
        While l is greater than or equal to 0
           and the key is less than the elements lower on the arrray
               Shift the array element up one.
        '''
        while l >=0 and key < arr[l]: 
            arr[l+1] = arr[l]
            l-=1
        arr[l+1] = key  # drop the key infront of the elements greater than it


if __name__ == "__main__":

    a = [6,4, 8, 0]
    print(a)
    insertion(a)
    print(a)

