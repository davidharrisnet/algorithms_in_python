
from algorithms_in_python.leetcode.trees_and_graphs import binary_tree_random
from algorithms_in_python.leetcode.trees_and_graphs.tree_node import TreeNode
class MaxDepthTree(binary_tree_random.BinaryTree):
    def __init__(self, arr=None):
        binary_tree_random.BinaryTree.__init__(self)
        if arr:
            for i in arr:
                self.insert(i)
            
    def max_depth_recursive(self):
        return self._max_depth_recursive(self.root)
                
    def max_depth_iterative(self):
        return self._max_depth_iterative(self.root)
  
        
    def _max_depth_iterative(self, node):
        
        if not node:
            return 0
        stack = [(node, 1)]
        ans = 0
        while stack:
            node,depth = stack.pop()
            ans = max(ans, depth)
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
                
        return ans
  
    def _max_depth_recursive(self, node) -> int:
        # Base Case 
        if not node:
            return 0
        
        # Assume method does something
        left = self._max_depth_recursive(node.left)   # This will recurse until the null leaf is found-
        right = self._max_depth_recursive(node.right) # This will recurse until the nul leaf is found
        
        print(f"val {node.val} -- left {left}  right {right}")
                
        return max(left, right) + 1  # pop each stack frame, returning the max depath plus one.


if __name__ == "__main__":
    
   
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(5)
    root.right = TreeNode(4)
    bt = MaxDepthTree()
    bt.root = root
    bt.printInorder()
    print(bt.max_depth_recursive())
    

        


