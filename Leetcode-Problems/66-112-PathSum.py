## 112 -- https://leetcode.com/problems/path-sum/


# Solution 1: not a good one

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root is None:
            return False
        
        # base case 
        # if current node is leaf, and its value is equal to targetSum, we found path
        if root.val == targetSum and root.left is None and root.right is None:
            return True
        
        # recursive case
               
        # recursive call for left and right child
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

'''
time complexity - O(n) -- in worst case we need to traverse each node
space complexity - O(n) - in worst 
'''
'''
Time complexity #
The time complexity of the above algorithm is O(N)O(N), where ‘N’ is the total number of nodes in the tree. This is due to the fact that we traverse each node once.

Space complexity #
The space complexity of the above algorithm will be O(N)O(N) in the worst case. This space will be used to store the recursion stack. The worst case will happen when the given tree is a linked list (i.e., every node has only one child).
'''
