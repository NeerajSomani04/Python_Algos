# Solution 1:

class Solution:
    ans = 0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.ans = -1
        self.solve(root)
        return self.ans
    
    def solve(self, root: TreeNode) -> int:
        if root is None:
            return 0
        lh = self.solve(root.left)
        rh = self.solve(root.right)
        self.ans = max(self.ans, lh+rh)
        return 1+max(lh,rh)
    
''' Big-O efficiency:
time complexity - O(n) - go through every node
space complexity - O(k) - stack frame , that hold at max k function at given time for a left or right subtree of the root node
'''
    
# Solution 2:

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def depth(root):
            if not root:
                return float('-inf'), 0
            left_global, left_local = depth(root.left)
            right_global, right_local = depth(root.right)
            global_mx = max(left_global, right_global, 1 + left_local + right_local)
            local_mx = 1 + max(left_local, right_local)
            return global_mx, local_mx
        if not root: 
            return 0
        global_mx, local_mx = depth(root)
        return global_mx - 1
