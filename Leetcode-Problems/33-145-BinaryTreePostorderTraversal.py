# In this we are going to solve leetcode #145 problem
# https://leetcode.com/problems/binary-tree-postorder-traversal/

# we are going to follow a specific process (D, D, P, A, B)
# Definition, Data, Pseudo code, Actual code, Big-O efficiency

## Definition -- Can be easily understood from leetcode problem statement

## Data (IOEA) -- Input, Output, Edge Cases, Assumptions
  # Input -- any string charachter is allowed
  # Output -- single interger (that represent index value of first unique charachter and "-1" if no unique charachter)
  # Egde Cases -- An array can be empty or An array can have no unique charachter
  # Assumptions -- An array can contain only alphabets in lowercase, and no numerical or special charachter

''' Pseudo code  --
'''

# Actual code --
# Solution 1: iteratively, using a flag to indicate whether the node has been visited or not.

def postorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []        
        if not root:
            return ans
        stack = [(root, False)]
        while stack:
            cur, visited = stack.pop()
            if not cur:
                continue
            if visited:
                ans.append(cur.val)
            else:
                stack.append((cur, True))
                stack.append((cur.right, False))
                stack.append((cur.left, False))
        return ans
        
## Same as above solution, but different way of writting:
class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def postorderTraversal(self, root):
        traversal, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    # add to result if visited
                    traversal.append(node.val)
                else:
                    # post-order
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))

        return traversal

        
        
# Actual code --
# Solution 2: iteratively, uses modified preorder (right subtree first). Then reverse the result.

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def postorderTraversal(self, root):
        traversal, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                # pre-order, right first
                traversal.append(node.val)
                stack.append(node.left)
                stack.append(node.right)

        # reverse result
        return traversal[::-1]
      
## Solution 3: Recursively
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        return [] if not root else self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

      
      
