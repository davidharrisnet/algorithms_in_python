from binary_tree import BinaryTreeInterface, Node


class BinarySearchTree(BinaryTreeInterface):
    
    def __init__(self):
        self.root:Node = None
        
    def add(self, data):
        node = Node(data)
        if node is None:
            return
        
        self.root = self.__add( self.root, node)
                
    def __add(self, root, node):

        # Base case: found a leaf node
        if root == None:
            root = node
        else:
            # Pick a subtree to insert element
            if node.data < root.data:
                root.left = self.__add(root.left, node)
            else:
                root.right = self.__add(root.right, node)

        return root

    def remove(self, elem):
        """
        Remove a value from this binary tree if it exists, O(n)
        """
        # Make sure the node we want to remove
        # actually exists before we remove it
        if self.contains(elem):
            self.root = self.__remove(self.root, elem)
            self.nodeCount -= 1
            return True

        return False


    def __remove(self, node, elem):

        if node == None:
            return None

        cmp = elem < node.data
        
        if elem == node.data:

            # This is the case with only a right subtree or
            # no subtree at all. In this situation just
            # swap the node we wish to remove with its right child.
            if node.left == None:

                rightChild = node.right

                node.data = None
                node = None

                return rightChild

            # This is the case with only a left subtree or
            # no subtree at all. In this situation just
            # swap the node we wish to remove with its left child.
            elif node.right == None:

                leftChild = node.left

                node.data = None
                node = None

                return leftChild

                # When removing a node from a binary tree with two links the
                # successor of the node being removed can either be the largest
                # value in the left subtree or the smallest value in the right
                # subtree. In this implementation I have decided to find the
                # smallest value in the right subtree which can be found by
                # traversing as far left as possible in the right subtree.
            else:

                # Find the leftmost node in the right subtree
                tmp = self.findMin(node.right)

                # Swap the data
                node.data = tmp.data

                # Go into the right subtree and remove the leftmost node we
                # found and swapped data with. This prevents us from having
                # two nodes in our tree with the same value.
                node.right = self.__remove(node.right, tmp.data)

                # If instead we wanted to find the largest node in the left
                # subtree as opposed to smallest node in the right subtree
                # here is what we would do:
                # Node tmp = findMax(node.left);
                # node.data = tmp.data;
                # node.left = self.__remove(node.left, tmp.data);

                # Dig into left subtree, the value we're looking
                # for is smaller than the current value
        elif cmp is True:
            node.left = self.__remove(node.left, elem)

        # Dig into right subtree, the value we're looking
        # for is greater than the current value
        elif cmp is False:
            node.right = self.__remove(node.right, elem)

        # Found the node we wish to remove
        else:
            return None

    def findMin(self, node):
        """
        Helper method to find the leftmost node (which has the smallest value)
        """
        while node.left is not None:
            node = node.left
        return node


    def findMax(self, node):
        """
        Helper method to find the rightmost node (which has the largest value)
        """
        while node.right is not None:
            node = node.right
        return node


    def contains(self, elem):
        """
        returns true is the element exists in the tree
        """
        return self.__contains(self.root, elem)


    def __contains(self, node, elem):
        """
        private recursive method to find an element in the tree
        """

        # Base case: reached bottom, value not found
        if node == None:
            return False

        cmp = elem < node.data

        if elem == node.data:
            return True

        # Dig into the left subtree because the value we're
        # looking for is smaller than the current value
        elif cmp is True:
            return self.__contains(node.left, elem)

        # Dig into the right subtree because the value we're
        # looking for is greater than the current value
        elif cmp is False:
            return self.__contains(node.right, elem)

        # We found the value we were looking for
        else:
            return True


    def height(self):
        """
        Computes the height of the tree, O(n)
        """
        return self.__height(self.root)


    def __height(self, node):
        """
        Recursive helper method to compute the height of the tree
        """
        if node == None:
            return 0
        return max(self.__height(node.left), self.__height(node.right)) + 1


    def print(self):
        self.inorder()
            
    def inorder(self):
        self.__inorder(self.root,spaces=0,level_space=5)
    
    def __inorder(self, node,spaces, level_space=5):
    
        if node is not None:
            spaces += level_space
            self.__inorder(node.left,spaces)
            for i in range(level_space, spaces): print(end = " ")  
            print("|" + str(node.data) + "|<")
            self.__inorder(node.right,spaces)
            

            
if __name__ == "__main__":
    
    arr = [5,6,7,4,3,2,8,0]
    print(arr)
    bst = BinarySearchTree()
    for a in arr:
        bst.add(a)
    bst.print()       