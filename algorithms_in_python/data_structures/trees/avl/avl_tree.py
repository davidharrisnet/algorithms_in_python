

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1
        self.count = 1 # for duplicates
        

class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if not node: # None values have a height of 0
            return 0
        return node.height

    def balance(self, node):
        if not node:
            return 0
        # left height - right height
        return self.height(node.left) - self.height(node.right)


    def insert(self, value):
        self.root = self.__insert(self.root, value)
        
    def __insert(self, parent, value):
        if not parent:
            return Node(value)
        elif value < parent.value:
            parent.left = self.__insert(parent.left, value) # recurse left
        elif value > parent.value:
            parent.right = self.__insert(parent.right, value) # recurse right
        else:
            parent.count += 1 # found a duplicate

        return self.rebalance(parent)

    def delete(self, parent, value):
        if not parent:
            return parent

        if value < parent.value:
            parent.left = self.delete(parent.left, value)
        elif value > parent.value:
            parent.right = self.delete(parent.right, value)
        else:
            if parent.count > 1:
                parent.count -= 1
                return parent
            elif not parent.left:                              
                temp = parent.right
                parent = None
                return temp
            elif not parent.right:
                temp = parent.left
                parent = None
                return temp

            temp = self.min_value_node(parent.right)
            parent.value = temp.value
            parent.right = self.delete(parent.right, temp.value)
        
        if not parent:
            return parent
        else:
            return self.rebalance(parent)

    def rebalance(self,parent):
              
        parent.height = 1 + max(self.height(parent.left), self.height(parent.right))
        balance = self.balance(parent)

        # Right rotationn (> 1 >=0)
        if balance > 1 and self.balance(parent.left) >= 0:
            return self.right_rotate(parent)
        
        # parent.left then Right rotation (> 1 < 0)
        if balance >  1 and self.balance(parent.left) < 0:
            parent.left = self.left_rotate(parent.left)
            return self.right_rotate(parent)

        # Left rotation (< -1 <=0)
        if balance < -1 and self.balance(parent.right) <= 0:
            return self.left_rotate(parent)

        # parent.right then Left rotation (< -1 > 0)
        if balance < -1 and self.balance(parent.right) > 0:
            parent.right = self.right_rotate(parent.right)
            return self.left_rotate(parent)

        return parent
    
    def left_rotate(self, node):
        
        """
        the balance of the left minus the right > 1
        
          A
           \
            C
            /  \
           D     E     
    
    
        # r = node.right    
        r =   C         
            /  \
           D     E  
           
        # temp = r.left
        temp = D
        
         # r.left  = node
         
             C
            / \
           A   E
            \
             C
            /  \
           D     E 
        
        # node.right = temp
                  
              C     
            /  \
           A    E
             \
              D
           
     
    # summary 
    # balance 
    
          A
            \
             C
            /  \
           D     E  
           
    # after left rotation 
    
             C    
            /  \
           A    E
             \
              D
        
    """
        
        r = node.right
        temp = r.left

        r.left = node
        node.right = temp

        node.height = 1 + max(self.height(node.left), self.height(node.right))
        r.height = 1 + max(self.height(r.left), self.height(r.right))

        return r

    def right_rotate(self, node):
        l = node.left
        temp = l.right

        l.right = node
        node.left = temp

        node.height = 1 + max(self.height(node.left), self.height(node.right))
        l.height = 1 + max(self.height(l.left), self.height(l.right))

        return l

    def min_value_node(self,parent):
        # recurse left until you hit the bottom
        current = parent
        while current.left:
            current = current.left
        return current

    def search(self, parent, value):
        if not parent or parent.value == value:
            return parent # found or at the bottom
        
        if value > parent.value:
            return self.search(parent.right, value) # search right
        else:
            return self.search(parent.left, value) # search left

    def delete_value(self, value):
        self.root = self.delete(self.root, value)

    def search_value(self, value):
        return self.search(self.root, value)
    
    def inorder(self):
        self.__inorder(self.root,spaces=0,level_space=5)
    
    def __inorder(self, node,spaces, level_space=5):
    
        if node is not None:
            spaces += level_space
            self.__inorder(node.left,spaces)
            for i in range(level_space, spaces): print(end = " ")          
            print("|" + str(node.value) + f" ({node.count})" + "|<")
            self.__inorder(node.right,spaces)

# Example usage:
if __name__ == "__main__":
    arr = [i for i in range(10) ]
    print(arr)
    tree = AVLTree()
    for i in arr:
        tree.insert(i)
    for i in arr:
        tree.insert(i)
    tree.inorder()
    

    print("Tree after insertion:")
    # In-order traversal to print the tree
    for i in arr:
        #tree.inorder()
        tree.delete_value(i)
    tree.inorder()
    print("-------------------------------")
    for i in arr:
        tree.inorder()
        tree.delete_value(i)