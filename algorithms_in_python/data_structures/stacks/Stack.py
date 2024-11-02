


class Stack():
    
    def __init__(self):
        self.stack = []

    def push(self, o):
        self.stack.append(o)
    
    def pop(self):
        self.stack.pop()
        
    def length(self):
        return len(self.stack)
    
    def clear(self):
        self.stack = []
        
    def __str__(self):
        return str(self.stack)

if __name__ == "__main__":
   
   s = Stack()
   s.push(4)
   s.push(5)
   s.push(6)
   print(s)
   s.pop()
   print(s)
   s.clear()