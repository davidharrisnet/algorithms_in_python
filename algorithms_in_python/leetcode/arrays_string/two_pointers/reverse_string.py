def string_reverse(arr):
    i = 0
    j = len(arr) -1
    
    while i < j:
        arr[i], arr[j] = arr[j] , arr[i]
        i += 1
        j -= 1
   

if __name__ == "__main__":
    arr =  ["H","a","n","n","a","h"]
   
    string_reverse(arr)
    print(arr)