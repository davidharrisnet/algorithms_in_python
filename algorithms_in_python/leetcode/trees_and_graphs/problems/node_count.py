from algorithms_in_python import lists, TreeNode
from algorithms_in_python.leetcode.trees_and_graphs.binary_tree_random import BinaryTree
from algorithms_in_python.leetcode.trees_and_graphs import bt1
from collections import deque
import sys

class NodeCount(BinaryTree):
    def __init__(self):
        BinaryTree.__init__(self)
        self.tree_nodes = []
    def nodeCount(self):        
        self.node_count(self.root,0)
    
    def node_count(self, root, targetSum):
        
        def dfs(node, curr):
            if not node:      # base case
                return 0
            
            
            # Pre-order business               
            
            curr += node.val
            self.tree_nodes.append((node.val,curr))
            
            dfs(node.left,curr)
            dfs(node.right, curr)
            
            
           
            
        dfs(root, targetSum)
        


bt = NodeCount()
root = bt1()
bt.root = root
bt.printInorder()
bt.nodeCount()
print(bt.tree_nodes)


