## 437 -- https://leetcode.com/problems/path-sum-iii/


# Solution 1:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, _sum: int) -> int:
        return self.findPaths(root, _sum, [])
        
    
    def findPaths(self, root: TreeNode, _sum, eachPath: list):
        if root is None:
            return 0
        # add the current node to the path
        eachPath.append(root.val)
        
        pathCount, pathSum = 0, 0
        
        # find the sum of all sub-paths in the current path list
        
        for i in range(len(eachPath)-1, -1, -1):
            pathSum += eachPath[i]
            
            if pathSum == _sum:
                pathCount += 1
                   
        pathCount += self.findPaths(root.left, _sum, eachPath)
        pathCount += self.findPaths(root.right, _sum, eachPath)
            
        eachPath.pop()
        
        return pathCount

'''
Time complexity #
The time complexity of the above algorithm is O(N^2) in the worst case, where ‘N’ is the total number of nodes in the tree. This is due to the fact that we traverse each node once, but for every node, we iterate the current path. The current path, in the worst case, can be O(N)O(N) (in the case of a skewed tree). But, if the tree is balanced, then the current path will be equal to the height of the tree, i.e., O(logN). So the best case of our algorithm will be O(NlogN).

Space complexity #
The space complexity of the above algorithm will be O(N). This space will be used to store the recursion stack. The worst case will happen when the given tree is a linked list (i.e., every node has only one child). We also need O(N)O(N) space for storing the currentPath in the worst case.

Overall space complexity of our algorithm is O(N).
'''
