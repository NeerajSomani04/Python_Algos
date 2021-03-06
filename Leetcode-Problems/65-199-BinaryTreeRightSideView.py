## 199 -- https://leetcode.com/problems/binary-tree-right-side-view/


# Solution 1: --

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        '''
        view = []
        if root:
            level = [root]
            while level:
                view += level[-1].val,
                level = [kid for node in level for kid in (node.left, node.right) if kid]
        return view
        '''
        if root is None:
            return 
        queue = [root]
        result = []
        while queue:
            len_level = len(queue)
            level_elements = []
            while len_level > 0:
                curr = queue.pop(0)
                len_level -= 1
                level_elements.append(curr.val)
                
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)  
            result.append(level_elements[-1])
        return result
        
'''
time complexity - O(n)
space compelxity - O(1) 
'''

