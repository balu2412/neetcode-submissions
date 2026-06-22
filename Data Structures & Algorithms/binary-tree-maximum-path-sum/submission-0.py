# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxi=float("-inf")
        def dfs(node):
            if node is None:
                return 0
            leftsum=max(0,dfs(node.left))
            rightsum=max(0,dfs(node.right))
            self.maxi=max(self.maxi,leftsum+node.val+rightsum)
            return node.val+max(leftsum,rightsum)
        dfs(root)
        return self.maxi