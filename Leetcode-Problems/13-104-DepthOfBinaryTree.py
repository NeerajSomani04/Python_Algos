# In this we are going to solve leetcode #104 problem
# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# we are going to follow a specific process (D, D, P, A, B)
# Definition, Data, Pseudo code, Actual code, Big-O efficiency

## Definition -- Can be easily understood from leetcode problem statement
# level order traversal meaning --> traversing left to right level by level
# This concept is also known as Breadth first search (BFS)

## Data (IOEA) -- Input, Output, Edge Cases, Assumptions
  # Input -- a root node representing binary tree
  # Output -- return a number that represent depth/height of tree
  # Egde Cases -- "None" as root node or even at any level on any node
  # Assumptions -- if root is "None", return an empty array []
  

# important point about this solution:-
# BFS problems mostly requires a use of Queue concept. Because queue can hold the nodes of tree in specific order that we need to process. example, queue holds node from left to right and process them in FIFO order basis.
# hence, we run our algorithm untill our queue is empty. 


''' Psudo code
  - if node is null, return 0
  - depth = max(go left, go right)
  - return 1+depth
'''

## Different approach
## Solution 1: using recursion and Depth First Search
class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

class Solution:
  def maxDepth(self, root):
    if root is None:
      return 0
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


'''
time complexity --> O(n) --> we look every node once
    --> to be more specific for explaining, O(n + 2k), where n is total number of nodes in tree and k is number of leaf nodes for which we check left and right null value nodes as well, hence "2k". But at the its comes down to O(n).
    
space complexity --> O(k) --> where k is height of tree, because at any given time stack will hold only nodes at any given height.
Runtime: 40 ms
Memory Usage: 16.2 MB
'''


## Solution 2: Using iterative approach and Breadth First Search
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        depth = 0
        queue = [root]
        while queue:
            bookmark = len(queue)
            while bookmark > 0:
                on = queue.pop(0)
                if on.left:
                    queue.append(on.left)
                if on.right:
                    queue.append(on.right)
                bookmark -= 1
            depth += 1
        return depth
  
 '''
time complexity --> O(n) --> we look every node once
    --> to be more specific for explaining, O(n + 2k), where n is total number of nodes in tree and k is number of leaf nodes for which we check left and right null value nodes as well, hence "2k". But at the its comes down to O(n).
    
space complexity --> O(k) --> at any given time, maximum items in queue will be items at any given level
Runtime: 44 ms
Memory Usage: 15.4 MB
'''

## important thing to understand -->
## Solution 2 on leetcode is much efficient than Solution 1, need to understand, how efficiency can be observed.


## Solution 3: DFS using stack (iterative), i need to test this solution
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        stack = []
        stack.append((root,1))
        ans = 0
        while stack:
            cur_root,depth = stack.pop()
            if depth > ans:
                ans = depth
            if cur_root.right:
                stack.append((cur_root.right,depth+1))
            if cur_root.left:
                stack.append((cur_root.left,depth+1))
        return ans

  
  
