from array import array

#https://docs.python.org/3/library/array.html

arr = array('l', [1, 2, 3, 4, 5]) # l signed long


arr.append(4)

class ArrayList():
    def __init__(self, arr:array, len:int, max:int):
        self.arr = arr
        self.len = len
        self.max = max
    def add(self,n:int):
        if self.len + 1 > self.max:
            self.max *= 2
            new_arr = 