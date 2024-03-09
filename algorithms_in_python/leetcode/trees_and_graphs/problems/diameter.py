
from algorithms_in_python.leetcode.trees_and_graphs import binary_tree
from algorithms_in_python.leetcode.trees_and_graphs.tree_node import TreeNode

class DiameterTree(binary_tree.BinaryTree):
    def __init__(self, arr=None):
        binary_tree.BinaryTree.__init__(self)
        if arr:
            for i in arr:
                self.insert(i)
    def height(self,node):        
        # Base Case : Tree is empty
        if node is None:
            return 0    
        # If tree is not empty then height = 1 + max of left
        # height and right heights
        return 1 + max(self.height(node.left), self.height(node.right))
             
        
    def diameter(self, node) -> int:
        # Base Case 
        if not node:
            return 0
        
        # Get the height of left and right sub-trees
        lheight = self.height(node.left)
        rheight = self.height(node.right)
         
        # Get the diameter of left and right sub-trees
        ldiameter = self.diameter(node.left)
        rdiameter = self.diameter(node.right)
                        
        # Return max of the following tree:
        # 1) Diameter of left subtree
        # 2) Diameter of right subtree
        # 3) Height of left subtree + height of right subtree +1
        current_diameter = lheight + rheight + 1
        max_diameter = max(ldiameter, rdiameter)
        #return max(lheight + rheight + 1, max(ldiameter, rdiameter))
        return max(current_diameter, max_diameter)


if __name__ == "__main__":
    
   
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    # root.left.right.left = TreeNode(6)
    root.left.right.right = TreeNode(8)
    root.left.left.left = TreeNode(13)
    root.left.left.left.left = TreeNode(14)
    root.left.right.right.right = TreeNode(10)
    #root.left.right.right.left = TreeNode(11)
    root.right = TreeNode(3)
    bt = DiameterTree()
    bt.root = root
    bt.printInorder()
    print(bt.diameter(root))
    

        


