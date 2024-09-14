import random

from algorithms_in_python.leetcode.trees_and_graphs.tree_node import TreeNode
    
class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self,val):
        if val == None:
            return
        newNode = TreeNode(val)
        if not self.root:            
            self.root = newNode
        else:
            self._insert(newNode, self.root)
       
    def _insert(self,newNode, currNode):
        if currNode.left is None and newNode.val < currNode.val:
            currNode.left = newNode 
        elif currNode.right is None and newNode.val >= currNode.val:
            currNode.right = newNode           
        else:                   
            if newNode.val <= currNode.val:
                self._insert(newNode, currNode.left)
            else:
                self._insert(newNode, currNode.right)
           
    def printInorder(self,show_tree=True):
        self._printInorder(self.root, show_tree=show_tree)
        
    def _printInorder(self, root, space=0, show_tree=True, LEVEL_SPACE = 5 ):
        '''
            self._printInorder(root.left)
            print(root.val)
            self._printInorder(root.right))
        '''
        if (root == None): 
            return
        else:
            if show_tree:
                space += LEVEL_SPACE
            self._printInorder(root.left, space=space,show_tree=show_tree)         
            if show_tree:
                for i in range(LEVEL_SPACE, space): print(end = " ")  
                print("|" + str(root.val) + "|<")
            else:
                print(root.val)
            self._printInorder(root.right, space=space, show_tree=show_tree)
           

                
    def printPostorder(self,show_tree=False):
        self._printPostorder(self.root, show_tree)
    '''    
    def _printPostorder(self,root):
        if root:
            self._printPostorder(root.left)
            self._printPostorder(root.right)
            print(root.val, end=" ")
    '''            
    def _printPostorder(self, root, space=0, show_tree=True, LEVEL_SPACE = 5):
        if (root == None): 
            return
        else:
            if show_tree:
              space += LEVEL_SPACE
            self._printPostorder(root.left, space, show_tree)                    
            self._printPostorder(root.right, space, show_tree)
            if show_tree:
                for i in range(LEVEL_SPACE, space): print(end = " ")  
                print("|" + str(root.val) + "|<")
            else:
                print(root.val)
            
    def printPreorder(self):
        self._printPreorder(self.root, show_tree=True)
        
    def _printPreorder(self, root, space=0, show_tree=True, LEVEL_SPACE = 5):
        '''
        print(root.val)
        self._printPreorder(root.left)
        self._printPreorder(root.right)
        '''
        if (root == None): 
            return
        else:
            if show_tree:
                space += LEVEL_SPACE
                for i in range(LEVEL_SPACE, space): print(end = " ")  
                print("|" + str(root.val) + "|<")
            else:
                print(root.val)
            self._printPreorder(root.left, space)                    
            self._printPreorder(root.right, space)
            
    def height(self):
        return self._height(self.root)
           
    def _height(self, root):
        #if root is None return 0
        if root==None:
            return 0
        #find height of left subtree
        hleft=self._height(root.left)
        #find the height of right subtree
        hright=self._height(root.right)  
        #find max of hleft and hright, add 1 to it and return the value
        if hleft>hright:
            return hleft+1
        else:
            return hright+1
        
    def balanced(self):
        return self._balanced(self.root)
        #if tree is empty,return True
    
    def _balanced(self,root):
        if root==None:
            return True
        #check height of left subtree
        lheight= self._height(root.left)
        rheight = self._height(root.right)
        #if difference in height is greater than 1, return False
        if(abs(lheight-rheight)>1):
            return False
        #check if left subtree is balanced
        lcheck=self._balanced(root.left)
        #check if right subtree is balanced
        rcheck=self._balanced(root.right)
        #if both subtree are balanced, return True
        if lcheck==True and rcheck==True:
            return True
        
if __name__ == "__main__":
    bt = BinarySearchTree()

    arr = [5,6,7,4,3,2,8,0]
    for i in arr:
        bt.insert(i)
        
    print("Inorder")
    bt.printInorder()
   
   
   
