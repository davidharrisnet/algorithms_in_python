from linked_list import LinkedListInterface
from node import DoubleNode

class DoublyLinkedList(LinkedListInterface):
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def add_head(self,new_node: DoubleNode):
        self.len += 1
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_tail(self,new_node: DoubleNode):
        self.len += 1
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def insert(self,new_node:DoubleNode,position:int):
        index = 0
        curr = self.head
        while curr and index < position:
            curr = curr.next
            index += 1
        if index == position:
           next = curr.next
           curr.next = new_node
           new_node.prev = curr

           new_node.next = next
           next.prev = new_node

        else:
            raise Exception(f"No index {position}")





    def remove_head(self):
        if self.head:
            self.head = self.head.next
            self.len -= 1

    def remove_tail(self):
        if self.tail:
            self.tail = self.tail.prev
            self.len -= 1

    def __str__(self):
        nodes = []
        if self.head is not None:
            curr_node = self.head
            while curr_node  != None:
                nodes.append(curr_node.data)
                curr_node = curr_node.next
        return " ".join([str(n) for n in nodes])

if __name__ == "__main__":
    nodes = [ DoubleNode(i) for i in list(range(0,10))]
    l = DoublyLinkedList();
    l.add_tail(nodes[0])
    l.add_tail(nodes[1])
    l.add_tail(nodes[2])
    l.add_tail(nodes[3])

    l.insert(nodes[8],2)
    print(l)
    while(l.len > 0):
        print(l)
        l.remove_head()