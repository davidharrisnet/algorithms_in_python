
from algorithms_in_python import lists, TreeNode
from binary_tree import BinaryTree
from algorithms_in_python.leetcode.trees_and_graphs import leet_code_bt
from collections import deque
import sys


class MinDepthTree(BinaryTree):
    def __init__(self):
        BinaryTree.__init__(self)

    def min_depth(self) -> int:
        return self.minDepth(self.root)
      
    def min_depth_good(self) -> int:
        return self.minDepth_good(self.root)
    

    
    def minDepth_good(self, root) -> int:
                   
        # Corner Case.Should never be hit unless the code is 
        # called on root = NULL
        if root is None:
            return 0

        # If right subtree is Null , recur for left subtree
        if root.right is None:
            return self.minDepth_good(root.left) +1
        
        # If left subtree is Null, recur for right subtree
        if root.left is None:
            return self.minDepth_good(root.right)+1



        return min(self.minDepth_good(root.left), self.minDepth_good(root.right))+1
    
    def bfs(self):
        self.bfs(self.root)
        
    def bfs(self, root):
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
        
tree = MinDepthTree()
arr = [3,9,20,None,None, 15,7]
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
tree.root = root
tree.printInorder()
min_height = tree.min_depth_good()
print(min_height)
print()
sys.exit(0)

tree = MinDepthTree()
arr = [2,None,3,None,4,None,5,None,6] 
for i in arr:
    tree.insert(i)
tree.printInorder()    

min_height = tree.min_depth_good()
print(min_height)
tree.bfs()
print()

root = leet_code_bt()
tree.root = root
min_height = tree.min_depth_good()
tree.printInorder()
print(min_height)
tree.minDepth_bfs()
