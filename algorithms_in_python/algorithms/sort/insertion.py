"""
[6, 4, 8, 0]
[4, 6, 8, 0] k = 1
[4, 6, 8, 0] k = 2
[0, 4, 6, 8] k = 3
"""


def insertion(arr):

    for i in range(1,len(arr)): 
        # k from  1 to the end of the array

        key = arr[i]  # select key at index                  
        print(key)
        j = i - 1      # select the previous index           
        
        '''
        While j is >= 0 and the arr[j] is > than key 
            move arr[j] up to arr[j+1] // move larger values up until arr[j] <= key
            j-=1
        place key in the spot past the last arr[j] <= key
        
        key = 6
        2,3,4,4,7 -> 2,3,4,6,7
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

