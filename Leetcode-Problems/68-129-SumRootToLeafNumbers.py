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
        
'''
Time complexity #
The time complexity of the above algorithm is O(N), where ‘N’ is the total number of nodes in the tree. This is due to the fact that we traverse each node once.

Space complexity #
The space complexity of the above algorithm will be O(N) in the worst case. This space will be used to store the recursion stack. The worst case will happen when the given tree is a linked list (i.e., every node has only one child).
'''
