 
from algorithms_in_python import lists
from binary_tree import BinaryTree


class GoodNode:
    def good_node(self, node, maxSoFar: float) -> bool:
      
        if not node:
            return
        
        
        curr += node.data
        left = self.good_node(node.left, curr)
        right = self.good_node(node.right, curr)
        return left or right
        
       

bt = BinaryTree()
arr = [1,2,3,4,5]
for i in arr:
    bt.insert(i)

bt.printInorder()

ps = GoodNode()

s = ps.good_node(bt.root, float("-inf"))
print(s)