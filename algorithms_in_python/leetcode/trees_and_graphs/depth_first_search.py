

from algorithms_in_python.leetcode.trees_and_graphs.binary_tree import BinaryTree
from algorithms_in_python.leetcode.trees_and_graphs.tree_node import TreeNode
from algorithms_in_python.utils import lists

root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(5)

root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.left.right.right = TreeNode(6)

def dfs(node):
    if node == None:
        return

    dfs(node.left)
    dfs(node.right)
    return

def preorder_dfs(node):
    '''
    In preorder traversal, logic is done on the current node before moving to the children
    '''
    if not node:
        return

    print(node.val, end=" ") # preorder - before
    preorder_dfs(node.left)
    preorder_dfs(node.right)
    return

def inorder_dfs(node):
    """
    For inorder traversal, we first recursively call the left child, then perform logic (print in this case)
    on the current node, and then recursively call the right child. 
    This means no logic will be done until we reach a node without a left child.
    """
    if not node:
        return

    inorder_dfs(node.left)
    print(node.val, end=" ")  # inorder - inside
    inorder_dfs(node.right)
    return


def postorder_dfs(node):
    """In postorder traversal, we recursively call on the children first and then perform logic on the current node. 
       This means no logic will be done until we reach a leaf node. 
       In a postorder traversal, the root is the last node where logic is done.
    """
    if not node:
        return

    postorder_dfs(node.left)
    postorder_dfs(node.right)
    print(node.val, end=" ")   # post order - afterwards
    return

if __name__ == "__main__":
    print("pre order")
    preorder_dfs(root)
    print()
    print("in order")
 
    
    inorder_dfs(root)
    print()
    print("post order")
    
    postorder_dfs(root)
    print()