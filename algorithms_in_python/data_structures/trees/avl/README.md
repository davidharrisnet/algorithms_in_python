# AVL Tree

### Height balanced binary search tree

Balance Factor = left subtree height - right subtree height

1. A balanced tree has a balance factor of {-1, 0, 1} 
|bf| >= 1 balanced
1. Balance factor of 2 means unbalanced left
|bf| > 1 inbalanced
   if inbalanced must rotate
```
def height(node):
    if node is None:
        return 0

    # compute the height of left and right subtrees
    lHeight = height(node.left)
    rHeight = height(node.right)

    return max(lHeight, rHeight) + 1

```

|**LL Inbalanced**|  **LL Rotation**|
|-----------------|--------------------------|
```
#  BF 1     BF 2           BF 0
   30       30              20 
  20      20             10   30
        10
```

|**RR Inbalanced**   |  **RR Rotation**|
|--------------------|--------------------------|

```  
BF -1    BG -2            BF 0
10        10               20
   20       20           20  30
              30
```

|**LR Inbalanced**   |  **LR Rotation**|
|--------------------|--------------------------|

```
    30           30           30          20
  10          10            20         10   30
                 20       10
```

**RL Inbalanced**
