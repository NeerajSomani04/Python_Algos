# 107 - https://leetcode.com/problems/binary-tree-level-order-traversal-ii/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return
        
        queue = [root]
        result = []
        
        while queue:
            len_q = len(queue)
            list_level = []
            while len_q > 0:
                curr = queue.pop(0)
                len_q -= 1
                list_level.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            result.append(list_level)
        
        return result[-1::-1]

'''
space complexity --> O(1) --> considering output levels array will always be there in any kind of solution, and level and queue will never go to n level and will always be comparativly small.
  -- also, it could be O(n) --> if we consider output array space in this calculation, the O(n+k), where n is number of nodes and k is maxinum size of queue.
time complexity --> O(n) --> because of upper while loop, inner while loop in only 'k' times which is maximum number of node at any given level.
'''    
