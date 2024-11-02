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
        
        
if __name__ == "__main__":
    mh = MaxHeap(10)
    arr = [None, 98,95,50,10,17,23]
    mh.arr = arr
    mh.last_index = len(arr) -1
    mh.insert(85)
    print(mh.arr)
       
    