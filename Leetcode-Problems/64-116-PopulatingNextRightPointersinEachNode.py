## 116 -- https://leetcode.com/problems/populating-next-right-pointers-in-each-node/


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return 
        
        queue = [root]
        
        while queue:
            len_level = len(queue)
            level_elements = []
            
            while len_level > 0:
                curr = queue.pop(0)
                len_level -= 1
                level_elements.append(curr)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
            #l = len(level_elements)
            for i in range(len(level_elements)-1):
                level_elements[i].next = level_elements[i+1]
            level_elements[len(level_elements)-1].next = None
        return root

'''
Time complexity #
The time complexity of the above algorithm is O(N)O(N), where ‘N’ is the total number of nodes in the tree. This is due to the fact that we traverse each node once.

Space complexity #
The space complexity of the above algorithm will be O(N)O(N), which is required for the queue. Since we can have a maximum of N/2N/2 nodes at any level (this could happen only at the lowest level), therefore we will need O(N)O(N) space to store them in the queue.
'''
