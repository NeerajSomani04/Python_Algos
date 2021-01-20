# In this we are going to solve leetcode #94 problem
# https://leetcode.com/problems/binary-tree-inorder-traversal/

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
# Solution 1: recursively

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:return []
        res = []
        res+=self.inorderTraversal(root.left)
        res.append(root.val)
        res+=self.inorderTraversal(root.right)
        return res

# Solution 2: Iteratively
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right

''' 
Big-O efficiency 
time complexity -- O(n)
space complexity -- O(n)
Leetcode statistics:
Runtime: 20 ms
Memory usage: 14.2 MB
'''

# Solution 3:- another iterative solution
def inorderTraversal(self, root):
    ans = []
    stack = []
    
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            tmpNode = stack.pop()
            ans.append(tmpNode.val)
            root = tmpNode.right
        
    return ans

''' 
Big-O efficiency 
time complexity -- O(n)
space complexity -- O(n)
Leetcode statistics:
Runtime: 32 ms
Memory usage: 14.3 MB
'''
