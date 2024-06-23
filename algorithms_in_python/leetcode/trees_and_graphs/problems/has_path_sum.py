 
from algorithms_in_python import lists
from binary_tree import BinaryTree


class PathSum:
    def hasPathSum(self, root, targetSum: int) -> bool:
        def dfs(node, curr):
            if not node:
                return False
            
            # if both children are null, then the node is a leaf
            if node.left == None and node.right == None:
                return (curr + node.data) == targetSum
            
            curr += node.data
            left = dfs(node.left, curr)
            right = dfs(node.right, curr)
            return left or right
        
        return dfs(root, 0)

bt = BinaryTree()
arr = [1,2,3,4,5]
for i in arr:
    bt.insert(i)

bt.printInorder()

ps = PathSum()

s = ps.hasPathSum(bt.root, 15)
print(s)