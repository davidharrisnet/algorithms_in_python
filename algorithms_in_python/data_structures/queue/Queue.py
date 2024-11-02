
capacity = 5
# maybe not complete, the start moves around for efficiency
class Queue():
    def __init__(self,capacity=5):
        self.q = [None] * 5
        self.size = 0
        self.capacity = capacity
        self.start = 0
        self.end = -1
        
    def add(self, val):
        if self.size < self.capacity:
            self.end = (self.end + 1) % self.capacity
            self.size += 1
            self.q[self.end] = val
            
    def remove(self):
        if self.size > 0 and self.size <= self.capacity:
            val = self.q[self.start]
            self.q[self.start] = None
            self.start += 1
            self.size -= 1
            return val
        
    def __str__(self):
        arr = []
         
        if self.end > self.start:
            i = self.start
            while i <= self.end:
                arr.append(self.q[i])
                i += 1
        if self.end < self.start:
            i = self.start
            while i < self.size:
                arr.append(self.q[i])
                i += 1
            i = 0
            while i <= self.end:
                arr.append(self.q[i])
                i += 1
        return str(arr)

        
if __name__ == "__main__":
    q = Queue()
    q.add(1)
    q.add(2)
    print(q)
    q.add(3)
    q.add(4)
    q.add(5)
    print(q)
    
    print(q.remove())
    print(q)
    print(q.remove())
    print(q)
    q.add(6)
    print(q)
    q.add(7)
    print(q)
    q.add(8)