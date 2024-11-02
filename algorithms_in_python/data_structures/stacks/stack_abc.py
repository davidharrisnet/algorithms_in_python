
from abc import ABC, abstractmethod

class Node:
    def __init__(self, data:int):
        self.next:Node = None
        self.data = data


class Stack(ABC):
    def __init__(self):
        self.head = None
        self.size = 0

    def empty(self):
        return self.size == 0
    def len(self):
        return self.size

    @abstractmethod
    def peek(self):
        pass

    @abstractmethod
    def push(self,new_node:Node):
        pass

    @abstractmethod
    def pop(self):
        pass

class LifoStack(Stack):
    def __init__(self):
        super().__init__()
    def peek(self):
        if self.head:
            return self.head.data
        else:
            return None

    def push(self, new_node: Node):

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def pop(self):
        if self.head:
            self.head = self.head.next
            self.size -= 1

    def __str__(self):
        nodes = []
        if self.head is not None:
            curr_node = self.head
            while curr_node  != None:
                nodes.append(curr_node.data)
                curr_node = curr_node.next
        return " ".join([str(n) for n in nodes])

if __name__ == "__main__":

    nodes = [Node(i) for i in list(range(0, 10))]
    l =  LifoStack();
    l.push(nodes[0])
    l.push(nodes[1])
    l.push(nodes[2])
    l.push(nodes[3])

    print(l)
    l.pop()
    print(l)
    l.push(nodes[3])
    print(l)
    l.pop()
    print(l)

    print(l.peek())
    print(l.peek())
    print(l.len())
    print(l.empty())

    while not l.empty():
        l.pop()
    print(l.empty())
