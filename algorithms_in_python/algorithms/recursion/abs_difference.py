

def abs_difference(arr1, arr2):
    assert(len(arr1) == len(arr2))
    if len(arr1) == 0:
        return 0
    
    return abs(arr1[0] - arr2[0])  + abs_difference(arr1[1:] , arr2[1:])
           
                                            
if __name__ == "__main__":
    arr1 = [1,2,3]
    arr2 = [4,5,6]
    diff = abs_difference(arr1, arr2)
    print(diff)
                            
                        