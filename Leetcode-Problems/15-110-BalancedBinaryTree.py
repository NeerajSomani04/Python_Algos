# In this we are going to solve leetcode #110 problem
## https://leetcode.com/problems/balanced-binary-tree/

# we are going to follow a specific process (D, D, P, A, B)
# Definition, Data, Pseudo code, Actual code, Big-O efficiency

## Definition -- Given a binary tree, determine if it is height-balanced. --> Can be easily understood from leetcode problem statement
For this problem, a height-balanced binary tree is defined as:
      -- a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

## Data (IOEA) -- Input, Output, Edge Cases, Assumptions
  # Input -- a root node representing binary tree
  # Output -- return true if balanced, else False
  # Egde Cases -- "None" as root node then return True
  # Assumptions --   

''' Psudo code
  - if root node is null, return True
  - get .left depth
  - get .right depth
  -- if difference > 1, return False
  -- recurse to left and right subtrees
'''

## Different approach
## Solution 1: 
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        if abs(leftDepth - rightDepth) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        depth = 0
        queue = [root]
        while queue:
            depth += 1
            bookmark = len(queue)            
            while bookmark > 0:
                on = queue.pop(0)
                if on.left:
                    queue.append(on.left)
                if on.right:
                    queue.append(on.right)
                bookmark -= 1
        return depth

'''
time complexity --> O(n^2) --> O(n * n) --> we look every node twice, once in the depth function and then run isBalanced function on every node.
    
space complexity --> O(n) --> because, in worst case, tree is perfectly unbalanced and become list, that will have to store n stack frame at any given time.
'''

