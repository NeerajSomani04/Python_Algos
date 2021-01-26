# In this we are going to solve leetcode #226 problem
# https://leetcode.com/problems/invert-binary-tree/

# we are going to follow a specific process (D, D, P, A, B)
# Definition, Data, Pseudo code, Actual code, Big-O efficiency

## Definition -- Can be easily understood from leetcode problem statement

## Data (IOEA) -- Input, Output, Edge Cases, Assumptions
  # Input -- root node of a tree
  # Output -- 
  # Egde Cases -- 
  # Assumptions -- 

''' Pseudo code  --
      
'''

# Actual code --
# Solution 1: recursive

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        
        root.left = right
        root.right = left
        
        return root
        
# Solution 2: iteratively
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return
        queue = [root]
        while queue:
            cur = queue.pop(0)
            cur.left, cur.right = cur.right, cur.left
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return root  
