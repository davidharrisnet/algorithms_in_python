

def inversion_count_brute_force(arr):
    inversions = []
    
    for index,i in enumerate(arr):
        for j in arr[index+1:]:
            if j < i:
                if (i,j) not in inversions:
                    inversions.append((i,j))
               
    return inversions
            
        



if __name__ == '__main__':
    # greatest number of inverions n(n-1)/2
    
    
    arr = [1, 3, 5, 2, 4, 6]
    
   
    ic = inversion_count_brute_force(arr)
    print(ic)
    
    
    
    
    
    
    
    
    
    
    
    