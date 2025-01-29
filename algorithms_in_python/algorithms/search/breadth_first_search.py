# Copilot!
import queue

"""
https://www.youtube.com/watch?v=pcKY4hjDrxk
https://www.udemy.com/course/datastructurescncpp/learn/lecture/13193676#content

Graph traversal methods.

Depth First Search
1. Visit
2. Exloration

"""


class Node:
    def __init__(self, val):
        self.val = val
        self.links = []
        self.visited = False

    def __iter__(self):
        return self.val


def connect(node1, node2):
    node1.links.append(node2)
    node2.links.append(node1)


def visit(node):
    print(node.val)
    node.visited = True

def visit(node):
    print(node.val, end=" ")  # visit

def bfs(node):
    visited = set()       # create an empty set
    q = queue.Queue()     # create the queue
    q.put(node)           # add the first node
    visited.add(node)     # add the node to visited

    while q.qsize() > 0:  # while the queue is not empty
        node = q.get()    # get the leftmost item ( FIFO )

        visit(node)       # visit

        for neighbor in node.links:       # get all the links
            if neighbor not in visited:   # not visited
                visited.add(neighbor)
                q.put(neighbor)


if __name__ == "__main__":
    '''    
           1
          /  \
         2    3
        / \   / \
       4   5  6  7
            \
             8
               \
                9
    '''


    def create_graph():
        node = {}
        print("------------------")
        for i in range(1, 10):
            node[i] = Node(i)
        print("_________________")
        connect(node[1], node[2])
        connect(node[1], node[3])
        connect(node[2], node[4])
        connect(node[2], node[5])
        connect(node[3], node[6])
        connect(node[3], node[7])
        connect(node[5], node[8])
        connect(node[8], node[9])

        return node




    print("depth")
    nodes = create_graph()

    bfs(nodes[1])
