class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node = None


class SinglyLinkedList:
    def __init__(self):
        self.head:Node = None  # empty list
        self.size:int = 0
    def add_end(self, new_node:Node):
        if self.head is not None:
            ptr_node = self.head
            while ptr_node.next is not None:
                ptr_node = ptr_node.next
            ptr_node.next = new_node
        else:
            self.head = new_node
        self.size += 1

    def remove_end(self):
        ptr_node = self.head
        while ptr_node is not Node:
            ptr_node = ptr_node.next
        ptr_node = None
        self.size -= 1

    def __str__(self):
        msg = []
        ptr_node = self.head
        while ptr_node is not None:
            msg.append(f"{ptr_node.data} ->")
            ptr_node = ptr_node.next
        msg.append("None")
        return  " ".join(msg)

if __name__ == "__main__":
    ssl = SinglyLinkedList()
    ssl.add_end(Node(1));
    ssl.add_end(Node(2));
    ssl.add_end(Node(3));
    print(ssl)
    ssl.remove_end();
    ssl.remove_end();
    ssl.remove_end();
    print(ssl)
