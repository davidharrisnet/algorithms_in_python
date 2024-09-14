
capacity = 5

class Queue():
    def __init__(self,capacity=5):
        self.q = [None] * 5
        self.size = 0
        self.capacity = capacity
        self.start = 0
        self.end = -1
        
    def add(self, val):
        if self.size < self.capacity:
            self.end += 1
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
        return 

        
if __name__ == "__main__":
    q = Queue()
    q.add(1)
    q.add(2)
    q.add(3)
    q.add(4)
    q.add(5)
    print(q)
    
    print(q.remove())
    print(q)