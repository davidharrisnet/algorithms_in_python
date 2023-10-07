class SingleNode:
    def __init__(self, data:int):
        self.next:SingleNode = None
        self.data = data

class DoubleNode:
    def __init__(self, data:int):
        self.next:DoubleNode = None
        self.prev: DoubleNode = None
        self.data = data

if __name__ == "__main__":
    n = SingleNode(1)
    n2 = DoubleNode(2)

