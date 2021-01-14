## Reverse a singly linked list.

# In this we are going to solve leetcode problem #700
# https://leetcode.com/problems/search-in-a-binary-search-tree/

# we are going to follow a specific process (D, D, P, A, B)
# Definition, Data, Pseudo code, Actual code, Big-O efficiency

## Definition -- Can be easily understood from leetcode problem statement

## Data (IOEA) -- Input, Output, Edge Cases, Assumptions
  # Input -- given a root node of a BST (meaning its balanced)
  # Output -- root node of sub-BST
  # Egde Cases -- only root node available
  # Assumptions -- If such a node does not exist, return null


''' 
Pseudo code  --
      - 
'''


# Actual code --
## Solution 1: iterative solution, also this is BFS solution
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        current_node = root
        while current_node != None:
            if current_node.val == val:
                return current_node
            elif current_node.val < val:
                current_node = current_node.right
            else:
                current_node = current_node.left
        return None

'''
## Big-O efficiency:
# time complexity -- O(n) -- because of while loop
Regardless of whether we use iteration or recursion, the time taken has a best case of O(1), if the node we're looking for was the root node, an average case of O(n-log-n) for a reasonably balanced tree, and a worst case of O(n) when the tree is long and stringy.
# space complexity -- 
It's best to use iteration rather than recursion here, because iteration is O(1) space, whereas recursion is O(log-n) on average with a worst case of O(n) space due to Python not supporting tail calls (meaning that everything goes on the stack, and that could be a lot for a stringy tree).
'''


## Solution 2: Recursive Solution and DFS solution
class Solution:
    def searchBST(self, root, val):
        if root and val < root.val: return self.searchBST(root.left, val)
        elif root and val > root.val: return self.searchBST(root.right, val)
        return root

'''
## Big-O efficiency:
# time complexity -- O(n) -- because of while loop
Regardless of whether we use iteration or recursion, the time taken has a best case of O(1), if the node we're looking for was the root node, an average case of O(n-log-n) for a reasonably balanced tree, and a worst case of O(n) when the tree is long and stringy.
# space complexity -- O(n) -- because of stack frame
'''      
