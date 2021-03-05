## 103 -- https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/


## Solution 1:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return
        
        queue = [root]
        result = []
        levelCount = 0
        while queue:
            len_level = len(queue)
            levelCount += 1
            level_elements = []
            while len_level > 0:
                curr = queue.pop(0)
                len_level -= 1
                level_elements.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
            if levelCount % 2 == 0:
                result.append(level_elements[-1::-1])
            else:
                result.append(level_elements)
        
        return result
                
'''
Time complexity #
The time complexity of the above algorithm is O(N)O(N), where ‘N’ is the total number of nodes in the tree. This is due to the fact that we traverse each node once.

Space complexity #
The space complexity of the above algorithm will be O(N)O(N) as we need to return a list containing the level order traversal. We will also need O(N)O(N) space for the queue. Since we can have a maximum of N/2N/2 nodes at any level (this could happen only at the lowest level), therefore we will need O(N)O(N) space to store them in the queue.
'''
