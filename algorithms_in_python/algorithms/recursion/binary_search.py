def binary_search(arr, target, low, high):
    global count
    count += 1
    if low > high:
        return False;
    else:
        mid = (low + high) // 2
        if target == arr[mid]:
            return True
        elif target < arr[mid]:

            return binary_search(arr,target,low,mid-1)
        else:
            return binary_search(arr,target,mid+1, high)




def binary_search(arr, term):
    index = len(arr) // 2
    def bin_search(arr,term,index):
        if len(arr) > index and arr[index] == term:
            return term

        else:
            
    return bin_search(arr,term,index)
        
        
    
if __name__ == "__main__":
    count = 0
    arr = list(range(0,1_000_000))
    found = binary_search(arr, 25, 0, len(arr)-1)
    print(found)
    print(count)