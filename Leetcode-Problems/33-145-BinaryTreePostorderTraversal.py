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
# Solution 1: iteratively

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
        
        
