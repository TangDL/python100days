

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        if not root: return 0

        res = 0
        def dfs(root):
            nonlocal res
            if not root: return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if left==0 and right==0:
                root.val = 1
            elif left == 1 or right == 1:
                root.val = 2
                res += 1
            else:
                root.val = 0
        dfs(root)
        return res
