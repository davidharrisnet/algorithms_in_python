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

from algs.datastructures.trees import binary_search_tree


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
