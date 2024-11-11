class MaxHeap():
    def __init__(self,heap_size:int):
        
        self.heap_size = heap_size
        self.last_index = 0
        self.arr = [ None] * self.heap_size
    
    def insert(self, val):
        if self.last_index == len(self.arr) -1:
            self.arr.append([None] * self.heap_size)
            
        self.last_index += 1
        self.arr[self.last_index] = val
        
        current = self.last_index
        parent = current // 2
        while parent >= 1 and (self.arr[parent] < self.arr[current]):
            self.arr[parent], self.arr[current] = self.arr[current], self.arr[parent]
            current = parent
            parent = current // 2
    def pop(self):
        if self.last_index == 0:
            return None
        # The greatest value to return
        max_value = self.arr[1] 
        
        # Swap out the root for the last element and shrink the heap
        self.arr[1] = self.arr[self.last_index] 
        self.arr[self.last_index] = None
        self.last_index -= 1
        
        # Bubble the root down
        
        for i in range(1,self.last_index):
            swap = 1
            if 2*i <= self.last_index and (self.arr[swap] < self.arr[2*1]):
                swap = 2*i+1
            if i != swap:
                self.arr[i], self.arr[swap] = self.arr[swap], self.arr[i]
            else:
                break
        return max_value
    def __repr__(self):
        return "[ " + " ".join([f"{i}," for i in self.arr[1:self.last_index]]) + \
                    f" {str(self.arr[self.last_index])} ]"
        
               
        
if __name__ == "__main__":
    mh = MaxHeap(10)
    arr = [98,95,50,10,17,23,85]
    for i in arr:
        mh.insert(i)    
    print(mh)
    print(mh.pop())
    print(mh)
    
       
    