
def find_sums_n_squared(sum, arr):
    sums = []

    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] + arr[j] == sum:
                sums.append((i,j))
    return sums

def find_sums(sum,arr):
    arr.sort(reverse=True)
    
    sums = []    
    i = 0
    while arr[i] > sum:
        i+=1
    j = i + 1
    
    while i < len(arr): 
        while j < len(arr):
            if arr[i] + arr[j] == sum:
                sums.append((i,j))                     
            j += 1
        i += 1
        j = i + 1 
    return arr, sums
        
            
arr = [20, 21, 1,2,15, 16, 3,4,50, 5,6]

arr, sums = find_sums(7, arr)
print(arr)
print(sums)




