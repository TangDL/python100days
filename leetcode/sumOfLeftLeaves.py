# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        def dfs(root):
            ans = 0
            if root.left and not root.left.left and not root.left.right:
                ans += root.left.val
            elif root.left:
                ans += dfs(root.left)
            if root.right and (root.right.right or root.right.left):
                ans += dfs(root.right)
            return ans
        res = dfs(root)
        return res