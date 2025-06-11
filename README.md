# Data Structures


##   Linear
###   Array
* Python has dynamic arrays.
    * append() adds to the end
    * pop() removes from the end (b = a.pop())
    * remove() -- removes the first occurance of an element
    * sorting --
        list.sort() is provided, but also sorted()
        * if a list has objects, sorted can work on any iterable

    ```
           sorted(a, key=lambda o : o['name'], reverse=True)
    ```
    * [cpython sort](https://github.com/python/cpython/blob/main/Objects/listsort.txt) -- optimized mergesort - timsort
###   Stack
* FIFO 
    * Can use python list append() pop()
    * Can use a linked list
    * Can use collections deque ( See Queue )
```
        import collections deque
        a = deque()
        a.append(1) # [1]
        a.append(2) # [1,2]
        a.pop() # [1]
```

    
###   Queue
* LIFO -- like a line 
* Can use list append(), pop(0)
    * This is O(N) so not advised for large lengths 
    *  Can use a linked list with pointers to the head and end node.

   * python has - collections deque
```
        import collections deque
        a = deque()
        a.append(1) # [1]
        a.append(2) # [1,2]
        a.popleft() # [2]
```
    
## Non Linear
### Trees
#### Binary Tree
##### Binary Search Tree

## Binary Tree
### Depth First Search

*   [Operations](https://www.geeksforgeeks.org/binary-tree-data-structure/)
*   Inorder Traversal
*   Preorder Traversal
*   Postorder Traversal

### Breadth First Search

## Balanced Binary Tree
* AVL Tree [Example](%5Bhttps://www.geeksforgeeks.org/avl-tree-in-python/%5D(https://www.datacamp.com/tutorial/avl-tree))
* B-Tree

*   [Discussion Programiz ](https://www.programiz.com/dsa/balanced-binary-tree)

### Balanced Search Trees:

[MIT](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/83cdd705cd418d10d9769b741e34a2b8_MIT6_006F11_lec06.pdf)

#### There are many balanced search trees.

1.  AVL Trees - Adelson-Velsii and Landis 1962
2.  B-Trees/2-3-4 Trees - .Bayer and McCreight 1972 (see CLRS 18
3.  BB\[ \] Trees - Nievergelt and Reingold 1973
4.  Red-black Trees - CLRS Chapter 13
    1.  Splay-Trees - Sleator and Tarjan 1985
    2.  Skip Lists - Pugh 1989
    3.  Scapegoat Trees - Galperin and Rivest 1993
    4.  Treaps - Seidel and Aragon 199

# Algorithms

### Top Algorithms/Problems

1.  Heap
    1.  Minimum
    2.  Maximum
2.  HashMaps
3.  Sliding Window
4.  Binary Search
5.  Recursion

## Sorting

1.  Sort ( Algorithms/Sort)
    1.  Insertion
    2.  Merge
    3.  Quick
        1.  Left
        2.  Right
        3.  Random

## Trees

1.  Binary Search Tree
2.  Bread-First Search
3.  Depth-First Search
    1.  In Order
    2.  Pre Order
    3.  Post Order
4.  Greedy Algorithm

## Lists

LinkedList

1.  Single
2.  Double

Queue

Stack

Priority Queue

## Problems

1.  Window
2.  Tree Depth