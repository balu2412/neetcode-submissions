# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        if not subroot:
            return True
        if not root:
            return False
        if self.issametree(root,subroot):
            return True
        return self.isSubtree(root.left,subroot) or self.isSubtree(root.right,subroot)
    def issametree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        if not root and not subroot:
            return True
        if root and subroot and root.val==subroot.val:
            return (self.issametree(root.left,subroot.left) and self.issametree(root.right,subroot.right))
        return False