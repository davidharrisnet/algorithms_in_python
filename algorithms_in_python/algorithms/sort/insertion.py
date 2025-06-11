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
        print(f"key: {key}")
        j = i - 1      # select the previous index j
        
        '''
        While j is greater than or equal to 0 
            and the key is less than the the value at index j
               move arr[j] tp arr[j+1]
         This will stop once key encounters arr[j] that is less than key.
         This is the correct place for key.
8
         '''
         
        while j >= 0 and arr[j] > key:                   
            arr[j+1] = arr[j]                             
            
            j-=1        
        # either j == -1 or arr[j] <= key
        arr[j+1] = key  # place the key after the element <= than it. [0]  4
        print(arr)
       
if __name__ == "__main__":

    a = [6,2, 4, 3, 8, 0]
    print(a)
    insertion(a)
    print(a)

