# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dm=0
        def fun(root):
            if root is None:
                return 0
            else:
                l=fun(root.left)
                r=fun(root.right)
                self.dm=max(self.dm,l+r)
                return 1+max(l,r)
        fun(root)
        return self.dm 