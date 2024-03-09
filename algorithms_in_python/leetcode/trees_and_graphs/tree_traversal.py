
from algorithms_in_python import lists
from algorithms_in_python.leetcode.trees_and_graphs import leet_code_bt
from binary_tree import BinaryTree

from tree_node import TreeNode

bt = BinaryTree()
root = TreeNode(0)
l= TreeNode(1)
r = TreeNode(2) 

root.left = l
root.right = r

l.left = TreeNode(3)
l.right = TreeNode(4)
l.right.right = TreeNode(6)
r.right = TreeNode(5)

leet_code_bt()

"""
r.right = TreeNode(2)
r.right.right=TreeNode(3)
r.right.right.right=TreeNode(4)
r.right.right.right.right=TreeNode(5)
"""

print("In Order")
bt._printInorder(root,show_tree=False)

"""
   print("Pre Order")
   bt._printPreorder(root,show_tree=False)
   print("Post Order")
   bt._printPostorder(root, show_tree=False)
"""