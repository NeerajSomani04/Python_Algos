# In this we are going to solve leetcode #617 problem
# https://leetcode.com/problems/merge-two-binary-trees/

# we are going to follow a specific process (D, D, P, A, B)
# Definition, Data, Pseudo code, Actual code, Big-O efficiency

## Definition -- Can be easily understood from leetcode problem statement

## Data (IOEA) -- Input, Output, Edge Cases, Assumptions
  # Input -- an array of integers
  # Output -- single interger (that unique single number)
  # Egde Cases -- 
  # Assumptions -- Each element in the array appears twice except for one element which appears only once.   

# Actual code --
# solution 1: Recursively

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 == None:
            return t2
        if t2 is None:
            return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1

''' Big-O efficiency
Space complexity - O(n) - because of recursive stack
time complexity - O(n) - need to read all nodes of tree which has minimum nodes
runtime - 84 ms
memory utilization - 15.2 MB
'''

# Solution 2: iterative approach

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 == None:
            return t2
        stack = []
        stack = [[t1,t2]]
        while stack:
            cur = stack.pop()
            if cur[0] == None or cur[1] == None:
                continue
            cur[0].val += cur[1].val
            if cur[0].left == None:
                cur[0].left = cur[1].left
            else:
                stack.append([cur[0].left,cur[1].left])
            if cur[0].right == None:
                cur[0].right = cur[1].right
            else:
                stack.append([cur[0].right,cur[1].right])
        return t1
    
''' Big-O efficiency
Space complexity - O(n) - because of hash table
time complexity - O(n) - Here, n refers to the smaller of the number of nodes in the two trees
runtime - 168 ms
memory utilization - 15.7 MB
'''
