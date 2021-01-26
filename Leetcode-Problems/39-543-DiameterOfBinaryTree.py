# Solution 1:

class Solution {
    int ans;
    public int diameterOfBinaryTree(TreeNode root) {
        if(root == null) return 0;
        ans = -1;
        solve(root);
        return ans;
    }
    private int solve(TreeNode root){
        if(root == null) return 0;
        int lh = solve(root.left);
        int rh = solve(root.right);
        ans = Math.max(ans,lh+rh);
        return 1+Math.max(lh,rh);
    }
}

class Solution:
    ans = 0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
    
      

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
