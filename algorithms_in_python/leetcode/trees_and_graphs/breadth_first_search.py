 
from algorithms_in_python import lists
from algorithms_in_python.leetcode.trees_and_graphs import leet_code_bt
from binary_tree import BinaryTree

from tree_node import TreeNode

from collections import deque

class Solution:
    def levelOrder(self, root):
        if not root: 
            return []
        queue, result = deque([root]), []
        
        while queue:
            level = []
            for i in range(len(queue)):
                print(queue[0].data, end = " ")
                node = queue.popleft()
                level.append(node.val)
                if node.left:  
                    queue.append(node.left)
                if node.right: 
                    queue.append(node.right)
            result.append(level)
        return result
 
import collections
"""
# BFS algorithm
def bfs(graph, root):

    visited, queue = set(), collections.deque([root])
    visited.add(root)

    while queue:

        # Dequeue a vertex from queue
        vertex = queue.popleft()
        print(str(vertex) + " ", end="")

        # If not visited, mark it as visited, and
        # enqueue it
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

if __name__ == '__main__':
    graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
    print("Following is Breadth First Traversal: ")
    bfs(graph, 0)
"""
    
bt = BinaryTree()

root = leet_code_bt()
bt.root = root

bt.printInorder()

s = Solution()
tree = s.levelOrder(root)
print()
for t in tree:
    print(t)