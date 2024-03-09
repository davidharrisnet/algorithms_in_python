
def line_count(node):
    if node.next is None:
        return 1
    
    return 1 + line_count(node.next)



class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
head = Node(0)
node = head
for i in range(1,10):
    node.next = Node(i)
    node = node.next

size = line_count(head)
print(size)
    