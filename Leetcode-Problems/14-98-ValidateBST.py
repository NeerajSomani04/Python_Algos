# In this we are going to solve leetcode #98 problem
# https://leetcode.com/problems/validate-binary-search-tree/

# we are going to follow a specific process (D, D, P, A, B)
# Definition, Data, Pseudo code, Actual code, Big-O efficiency

## Definition -- Can be easily understood from leetcode problem statement

## Data (IOEA) -- Input, Output, Edge Cases, Assumptions
  # Input -- a root node representing binary tree
  # Output -- return true if valid BST, else return False
  # Egde Cases -- "None" at any level on any node
  # Assumptions -- 
      -- if there is Null node, return True 
      -- if 2 equal values node than return False
     

'''
A valid BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Depth First Traversals:
(a) Inorder (Left, Root, Right) : 4 2 5 1 3
(b) Preorder (Root, Left, Right) : 1 2 4 5 3
(c) Postorder (Left, Right, Root) : 4 5 2 3 1
'''

my initial though DFS, will give faster result


''' Psudo code
  - if node is null, return True
  - if node out of range return False
  - validate left recursively
    - && validate right recursively
'''




## Different approach
## Solution 1: using recursion and Depth First Search (pre-order traversal)
class Solution:
    def isValidBST(self, root: TreeNode, min = float('-inf') , max = float('inf')  ) -> bool:
        if root is None:
            return True
        if root.val <= min or root.val >= max:
            return False            
        return self.isValidBST(root.left, min, root.val) and self.isValidBST(root.right, root.val,max)
          
                  
'''
time complexity --> O(n) --> we look every node once
    --> to be more specific for explaining, O(n + 2k), where n is total number of nodes in tree and k is number of leaf nodes for which we check left and right null value nodes as well, hence "2k". But at the its comes down to O(n).
    
space complexity --> O(n) --> O(3k) --> where k is height of tree, but at every level, it can have 3 stacks for root, left and right node. 

'''


