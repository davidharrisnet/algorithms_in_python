class ArrayList:
    def __init__(self, capacity = 10):
        self.size = capacity
        self.__arr = [None] * capacity # this is not static. its a list ..
