
class Node:
    def __init__(self,data):
        self.data = data
        self.next:Node = None
    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head:Node = None
        self.length:int = 0

    def find_end(self):
        curr_node = self.head       # head is not None
        next_node = self.head.next  # this might be None
        while next_node is not None:
            curr_node = next_node
            next_node = next_node.next
        return curr_node
    def add_end(self,new_node:Node):
        if self.head is None:
            self.head = new_node
        else:
            curr_node = self.head # head is not None
            next_node = self.head.next # this might be None
            while next_node is not None:
                curr_node = next_node
                next_node = next_node.next
            curr_node.next = new_node
        self.length += 1
    def remove(self,node:Node):
        




    def add_front(self,new_node:Node):
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def remove_front(self):
        if self.head is not None:
            self.head = self.head.next

    def remove_end(self):
        if self.head is None:
            return None
        elif self.head.next is None:
            self.head = None
            return None
        else:
            second_last = self.head
            while second_last.next.next is not None:
                second_last = second_last.next
            second_last.next = None
            return self.head
    def __str__(self):

        if self.head is None:
            return "None"
        else:
            message = []
            curr_node = self.head
            while curr_node is not None:
                message.append(f"{curr_node} -> ")
                curr_node = curr_node.next
            message.append("None")
            return "".join(message)

ll = LinkedList()
for i in range(0,10):
    n = Node(i)
    ll.add_end(n)
print(ll)
for i in range(0,10):
    ll.remove_front()
    print(ll)

ll = LinkedList()
for i in range(0,10):
    n = Node(i)
    ll.add_front(n)
print(ll)
for i in range(0,10):
    ll.remove_end()
    print(ll)



