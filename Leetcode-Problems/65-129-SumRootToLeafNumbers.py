## 129 -- https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Solution 1:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        result = []
        self.findAllPaths(root, [], result)
        sum = 0
        for i in result:
            sum = sum + int(''.join(str(x) for x in i))
        return sum
        
    def findAllPaths(self, root: TreeNode, eachPath: list, result: list):
        if root is None:
            return
        
        eachPath.append(root.val)
        
        if root.left is None and root.right is None:
            result.append(eachPath[:])
        else:
            self.findAllPaths(root.left, eachPath, result)
            self.findAllPaths(root.right, eachPath, result)
        
        eachPath.pop()
        
        
