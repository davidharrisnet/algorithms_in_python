import queue

"""
https://www.youtube.com/watch?v=pcKY4hjDrxk

Graph traversal methods.

Breadth First Search    
1. Visit
2. Exloration

 5   4        7  6 
  \ /          \/ 
   1------------2--------3 
   
   
BFS: 1, 2, 4, 5, 7, 3, 6
DFS: 1, 2, 3, 6, 7, 4, 5



           1
          /  \
         2    3
        / \  / \
       4   5 6  7    
 
 BFS: 1, 2, 3, 4, 5, 6, 7
 DFS: 1, 2, 4, 5, 3, 6, 7
"""



class Node:
    def __init__(self, val):
        self.val = val
        self.links = []
        self.visited = False

def connect(node1, node2):
    node1.links.append(node2)
    node2.links.append(node1)

five = Node(5)
four = Node(4)
one = Node(1)

connect(five,one)
connect(four(one))

seven = Node(7)
six = Node(6)
two = Node(2)
connect(seven, two)
connect(six, two)

connect(one,two)
three = Node(3)
connect(two, three)


q = queue.Queue()
# BFS
def visit(node, val):
    
    if node.val == val:
        return True
    else:
        q.get()
    
def breadth_first_search(node,val):
    q.put(node)
    if visit(node, val):
        return True
    else:
        for n in node.links:
            q.put(node)
        
        visit(node,val)
    