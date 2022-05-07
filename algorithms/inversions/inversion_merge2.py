import os

class InversionCount :
    
    def __init__(self):
        self.inversion_count = 0

    def sort(self, arr, left, right):
        
        if left < right:
            
            middle = int(left + (right-left)/2)
           
            self.sort(arr, left, middle)
            self.sort(arr, middle + 1, right)
 
            
            self.merge(arr, left, middle, right)
        	

	        
    def merge(self, arr, l, m, r):
    		        
        left_size = m - l + 1
        right_size = r - m
 
        
        L =  [None] * left_size
        R =  [None] * right_size
 
       
        for i in range(left_size):
            L[i] = arr[l + i];
        
        for j in range(right_size):
            R[j] = arr[m + 1 + j]
 
       
        
        i = 0 
        j = 0
 
       
        k = l
        while i < left_size and j < right_size:
            if L[i] <= R[j]: 
                arr[k] = L[i]
                i = i + 1
            
            else:
                arr[k] = R[j];
               
                j = j + 1
                leftInL = left_size -i ;
                    
                self.inversion_count = self.inversion_count + leftInL
                                                                            
            k = k + 1
        
 
        
        while i < left_size:
            arr[k] = L[i]
            i = i + 1
            k = k + 1          
        
 
        
        while j < right_size:
            arr[k] = R[j]
            j += 1
            k += 1
           
       
    def inversionCount(self, arr, left, right):	    
	    self.sort(arr, left, right)

 
if __name__ == "__main__":
   
    #arr = [1, 3, 5, 2]
    here = os.getcwd()
    textfile = os.path.join(here,"algorithms", "inversions", "IntegerArray.txt")
    
    f = open(textfile,"r")
    text = f.readlines()
    arr = [ int(t.replace('\n','')) for t in text ]

    ob = InversionCount()
    x = ob.inversionCount(arr, 0, len(arr) -1)


    
    #print(arr)
    print(ob.inversion_count)
