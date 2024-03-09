class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        

class SinglyLinkedList():
    def __init__(self):
        self.head = None
    
    def add(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
        else:
            currNode = self.head
            nextNode = self.head.next
            while nextNode:
                currNode = nextNode
                nextNode = nextNode.next
            currNode.next = newNode
    
    def __str__(self):
        result = []
        currNode = self.head
        while currNode:
            result.append(f" {currNode.data} ->")
            currNode = currNode.next
        result.append("None")
        return "".join(result)
        

sl = SinglyLinkedList()
sl.add(1)
sl.add(2)
sl.add(3)
print(sl)