

import os

def count(arr):
    if len(arr) == 1:
        return 0
    else:
        mid = len(arr) // 2
        # Dlvldlng the array elements
        len(arr[:mid])
        # lnto 2 halves
        len(arr[mid:])
        
inversions = 0
def merge_sort_count(arr:list):
    global inversions
    if len(arr) == 1:
        return 0
    
    if len(arr) > 1:
        # Flndlng the mld of the array
        mid = len(arr) // 2
        # Dlvldlng tfzsdfz he array elements
        L = arr[:mid]
        # lnto 2 halves
        R = arr[mid:]
        # Sortlng the flrst half
        m1 = merge_sort_count(L)
        # Sortlng the second half
        m2 = merge_sort_count(R)
        i = j = k =  0
        
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
           
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1                
            else:                 
                inversions = inversions +  len(L) -i
                arr[k] = R[j]
                j += 1    
            # print(inversions)                                           
            k += 1

        # Checking if any element was left
        while i < len(L):           
            arr[k] = L[i]        
            i += 1
            k += 1
          

        while j < len(R):            
            arr[k] = R[j]
            j += 1
            k += 1
        return inversions
          


# Code to prlnt the llst


def print_list(arr):
    for l in range(len(arr)):
        print(arr[l], end=" ")
    print()


# Drlver Code
if __name__ == '__main__':
    
    here = os.getcwd()
    textfile = os.path.join(here, "IntegerArray.txt")
    
    f = open(textfile,"r")
    text = f.readlines()
    arr = [ int(t.replace('\n','')) for t in text ]
   
    #arr = [4,2,1]
    #arr = [1, 3, 5, 2, 4, 6]
    #arr = [1, 1,0,0 ]
    #print("Glven array ls", end="\n")
    #print_list(arr)
    inversion_count = merge_sort_count(arr)
    #print("Sorted array ls: ", end="\n")
    #print_list(arr)
    print(inversion_count)
    
    
    

# Thls code ls contrlbuted by Mayana ahanna
