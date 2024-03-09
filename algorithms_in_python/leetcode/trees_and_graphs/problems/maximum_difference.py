
from algorithms_in_python.leetcode.trees_and_graphs import binary_tree
from algorithms_in_python.leetcode.trees_and_graphs.tree_node import TreeNode

class MaxDifferenceTree(binary_tree.BinaryTree):
    def __init__(self, arr=None):
        binary_tree.BinaryTree.__init__(self)
        self.res = 0
        if arr:
            for i in arr:
                self.insert(i)
                
            
    def max_diff_recursive(self):
        return self._max_diff_recursive(self.root)
                
      
    def _max_diff_recursive(self, root: TreeNode) -> int:
        if not root:
            return 0

        def helper(node, cur_max, cur_min):
            # if encounter leaves, return the max-min along the path
            if not node:
                return cur_max - cur_min
            # else, update max and min
            # and return the max of left and right subtrees
            cur_max = max(cur_max, node.val)
            cur_min = min(cur_min, node.val)
            left = helper(node.left, cur_max, cur_min)
            right = helper(node.right, cur_max, cur_min)
            return max(left, right)

        return helper(root, root.val, root.val)


if __name__ == "__main__":
    
   
    root = TreeNode(8)
    root.left = TreeNode(3)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(6)
    root.left.right.left = TreeNode(4)
    root.left.right.right = TreeNode(7)
    root.right = TreeNode(10)
    root.right.right = TreeNode(14)
    root.right.right.left = TreeNode(13)
    
    bt = MaxDifferenceTree()
    bt.root = root
    bt.printInorder()
    print(bt.max_diff_recursive())
    

        


