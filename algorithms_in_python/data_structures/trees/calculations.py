
# Catalan Number
# The number of binary trees for a given number of nodes

import math

def catalan_direct(n):
    if n < 0:
        return 0
    return math.factorial(2 * n) // (math.factorial(n + 1) * math.factorial(n))

nodes = [0, 1, 2, 3, 4, 5, 6]
for n in nodes:
    print(f"{n}: {catalan_direct(n)}")

# Tree terminology
# Root - the top
# Parent - the noe above
# Child - a node below
# Siblings - children of shared parent
# Descendants - All nodes below -- children and their children
# Ancestors -- All nodes to the Root -- parent and their parent
# Degree of a node - the number of children.
# Degree of a tree - The maximum degree of any node. 
# Leaf/External - no children
# Internal -- non leaf
# Height of a tree - number of edges of the longest path
 
# Level of a tree - Number of Nodes to the top inclusive. Root is level 1.
# Height of a Node - the number of edges from the botttom
# Depth of a Ndode - the number of edges from the top
# Forest -- a collection of Trees

# https://www.geeksforgeeks.org/find-the-maximum-depth-or-height-of-a-tree/
# Returns height - the number of edges along the longest path from the root 
# node down  to the farthest leaf node.

def height(node):
    if node is None:
        return 0

    # compute the height of left and right subtrees
    lHeight = height(node.left)
    rHeight = height(node.right)

    return max(lHeight, rHeight) + 1

# A Binary tree has at most 2 children. { 0, 1, 2}

# Binary Search Tree
# Binary
# All left nodes less than parent
# All right nodes greater than parent

from algorithms_in_python import BinarySearchTree, Node

arr = [5,6,7,4,3,2,8,0]

bst = BinarySearchTree()
for a in arr:
    bst.add(a)
bst.print()
print(bst.height())
print(height(bst.root))

# Given the height of a binary tree what is the maxiumum
# and minimum number of nodes. For instance a height of 2
# is a minimum of 3 and a maximum of 7 nodes
# 1) The minumum is the height + 1
# 2) The maximum is 2^h + 2^(h-1)... 2^0
def max_nodes(n):
    # geometric progression
       
    total = 0
    while n >= 0:
        total += 2**(n)
        n-=1
    return total
for h in nodes:
  print(f"{h}: {max_nodes(h)}")
  
# OR 2^(h+1) -1
numbers = []
for h in nodes:
    print( f"{h}: { 2**(h+1) -1}")
    numbers.append(2**(h+1) -1)
    

# If we know the number of nodes, N, the maximum height is N-1
# The minum height is log2(N + 1) -1
for n in numbers:
    print(f"{n} :  min {int(math.log2(n + 1) - 1)} :  max {n-1}")
    
# The range of heights for a binary tree, then is 
# log2(n+1) -1 to n -1
# or O(log2(n)) to O(n)

# Types of Binary Trees
# Strict binary each node has a degree of 0 or 2 nodes. ( Not 1)
# max nodes is the same 2^(height+1) -1
# minumim nodes = 2 * height + 1

# min height is log2(n+1) -1
# max height is ( n - 1) / 2
# So h
