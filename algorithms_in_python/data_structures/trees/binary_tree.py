

class Node():

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        

class BinaryTreeInterface:
    def __init__(self):
        self.height = 0
        self.balanced = None
        raise Exception("Can not instantiate BinryTreeInterface!")

    def add(self):
        pass
    def remove(self):
        pass      
    
