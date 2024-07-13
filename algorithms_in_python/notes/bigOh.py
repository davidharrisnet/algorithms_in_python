
'''

 Big Oh Examples
 
 Classic examples:
 finding all subsets of a set O(2**n)
 
 finding all permutations of a string O(n!)

 soring usign merge sort O(nlogn) 

 iterating over all cells in a matrix of size n*m == O(nm)

 '''
n = 1000
 
 # O(n)

for i in range(0, n):
    pass

# O(n**2)
for i in range(0,n):
    for j in range(0,n):
        pass
    

# n + n-1 + n-2 ... + 3,2,1
# n(n+1)/2 == n**2
for i in range(0,n):
    for j in range(i,n):
        pass
    
# binary search
# O(logn)
def binary_search(n, arr, low, high):
    while low < high:
        mid = (low + high) // 2  # get the mid point between low and high
        if arr[mid] == n:  
            return mid     # we found it
        elif n > arr[mid]:
            low = mid + 1   # n is less than arr[mid] so search on the lower half
        elif n < arr[mid]:
            high = mid + 1  # n is greater than arr[mid] so search on the greater half
        
    return -1
arr = [i for i in range(0,100)]    
n = 1
#print(n)
#print(arr[binary_search(n, arr, 0, len(arr)-1)])


# n + ( 3n + 2n) = 5n*2 == n**2
i = 0
while i < n:
    j = 0
    while j < 3*n:
        j = j + 1
    j = 0
    while j < 2*n:
        j = j + 1
    i += 1
    

i = 0
while i < 3*n:                # 3n
    j = 10
    while j <= 50:           # ( 40 + n**3)
        j += 1
    j = 0
    while j < n**3:
        j += 2
    i += 1
    # 3n * ( 40 + n**3/2) == n**4
        
        