

from algorithms_in_python.leetcode.trees_and_graphs.tree_node import TreeNode
from algorithms_in_python.leetcode.trees_and_graphs import binary_tree_random

def leet_code_bt():
    
    root = TreeNode(0)
    l= TreeNode(1)
    r = TreeNode(2) 

    root.left = l
    root.right = r

    l.left = TreeNode(3)
    l.right = TreeNode(4)
    l.right.right = TreeNode(6)
    r.right = TreeNode(5)
   
    return root    

def bt1():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    return root