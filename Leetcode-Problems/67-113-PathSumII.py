# 113 - https://leetcode.com/problems/path-sum-ii/

# Solution 1:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        result = []
        # at the start of the process "eachPath list is empty"
        # and result is also empty
        self.eachPathList(root, targetSum, [], result)
        return result
    
    def eachPathList(self, root: TreeNode, targetSum: int, eachPath: list, result:list):
        if root is None:
            return
        
        # add the current node to the path
        eachPath.append(root.val)
        
        # if current node is leaf and its value is equal to targetSum save the path
        if root.val == targetSum and root.left is None and root.right is None:
            result.append(eachPath)
            
        else:
            # traverse the left sub-tree
            self.eachPathList(root.left, targetSum - root.val, eachPath, result)
            # traverse the right sub-tree
            self.eachPathList(root.right, targetSum - root.val, eachPath, result)
        
        # remove the current node from the path for backtrack
        # also, we need to remove current node, while going up the recursive call track
        eachPath.pop()

'''
Time complexity #
The time complexity of the above algorithm is O(N^2), where ‘N’ is the total number of nodes in the tree. This is due to the fact that we traverse each node once (which will take O(N)O(N)), and for every leaf node we might have to store its path which will take O(N)O(N).

We can calculate a tighter time complexity of O(NlogN)O(NlogN) from the space complexity discussion below.

Space complexity #
If we ignore the space required for the allPaths list, the space complexity of the above algorithm will be O(N)O(N) in the worst case. This space will be used to store the recursion stack. The worst case will happen when the given tree is a linked list (i.e., every node has only one child).
'''
