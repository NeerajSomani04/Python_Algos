# In this we are going to solve leetcode #144 problem
# https://leetcode.com/problems/binary-tree-preorder-traversal/

# we are going to follow a specific process (D, D, P, A, B)
# Definition, Data, Pseudo code, Actual code, Big-O efficiency

## Definition -- Can be easily understood from leetcode problem statement

## Data (IOEA) -- Input, Output, Edge Cases, Assumptions
  # Input -- given root node for Binary tree
  # Output -- return tree nodes in pre-order traversal format
  # Egde Cases -- root node can be "None"
  # Assumptions -- 

''' Pseudo code  -- here, we will do BFS
      - if root:
        - create an array "result", add root into it
        - add left and right node values in result
        - go through each level
'''

# Actual code --
# Solution 1:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ret = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                ret.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return ret
        
'''
Big-O efficiency:
time complexity --> O(n) --> n is number of nodes
space complexity --> O(n) --> 
Leetcode statistics:
Runtime: 28 ms
Memory Usage: 14 MB
'''

# Solution 2: # recursively
def preorderTraversal1(self, root):
    res = []
    self.dfs(root, res)
    return res
    
def dfs(self, root, res):
    if root:
        res.append(root.val)
        self.dfs(root.left, res)
        self.dfs(root.right, res)
