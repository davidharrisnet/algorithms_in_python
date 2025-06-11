# Graphs and Trees

* A **graph** is comprised of  of **nodes** and **edges**.
* A **tree** is a graph with a single root and no cycles.
* The **height** of a node is the greatest count of **edges** from that node to a **leaf node**.
* A **leaf** node has a height of zero.
* The **height of the tree** is the height of the tree's **root node**
* An node's **depth** is the number of edges to the trees root.
* The depth of the tree is the maximum depth of any node in the tree.
* The tree's root has a depth of zero.
* The height of a tree is equal to the depth of the deepest node.

```
       A
      / \
     B   C
    / \ 
   D   E
```

   * **A** Depth: 0, Height 2
   * **C** Depth 1, Height 0
   * **B** Depth 1, Height 1
   * **D** Depth 2, Height 0
   * **E** Depth 2, Height 0
   * The tree has a depth of 2 because the deepest leafs are D and E and both have a depth of 2.

## Types of Trees
* **Full** Every internal node (non-leaf) has exacly two children
* **Complete** 

AI ..,

Full Tree:
.
Every internal node (non-leaf node) has exactly two children. It's also sometimes referred to as a strict binary tree. 
Complete Tree:
.
All levels are fully filled except possibly the last level, and the last level is filled from left to right. 
Perfect Tree:
.
Every internal node has exactly two children, and all leaf nodes are at the same level. A perfect tree is always both a full and complete tree, but a full or complete tree is not necessarily perfect. 
Degenerate Tree:
.
Every internal node has only one child. This is also known as a pathological tree. 
Balanced Tree:
.
The height difference between the left and right subtrees of every node is at most one. 
