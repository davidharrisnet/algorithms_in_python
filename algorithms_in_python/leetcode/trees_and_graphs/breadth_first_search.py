 
from algorithms_in_python.utils import lists
from algorithms_in_python.leetcode.trees_and_graphs import leet_code_bt
from algorithms_in_python.leetcode.trees_and_graphs.binary_tree_random import BinaryTreeRandom

from tree_node import TreeNode

from collections import deque

class Solution:
    def levelOrder(self, root):
        if not root: 
            return []
        queue, result = deque([root]), []
        
        while queue:
            level = []
            for i in range(len(queue)):
                print(queue[0].val, end = " ")
                node = queue.popleft()
                level.append(node.val)
                if node.left:  
                    queue.append(node.left)
                if node.right: 
                    queue.append(node.right)
            result.append(level)
        return result
 



bt = BinaryTreeRandom()

root = leet_code_bt()
bt.root = root

bt.printInorder()

s = Solution()
tree = s.levelOrder(root)
print()
for t in tree:
    print(t)