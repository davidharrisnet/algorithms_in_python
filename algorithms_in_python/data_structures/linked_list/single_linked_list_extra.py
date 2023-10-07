from algorithms_in_python.data_structures.linked_list.node import SingleNode

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def add_head(self,new_node: SingleNode):
        self.len += 1
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def add_tail(self,new_node: SingleNode):
        self.len += 1
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def remove_head(self):
        if self.head:
            self.head = self.head.next
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
    nodes = [ SingleNode(i) for i in list(range(0,10))]
    l = SingleLinkedList();
    l.add_head(nodes[0])
    l.add_tail(nodes[1])
    l.add_head(nodes[2])
    l.add_head(nodes[3])
    print(l)
    while(l.len > 0):
        l.remove_head()


