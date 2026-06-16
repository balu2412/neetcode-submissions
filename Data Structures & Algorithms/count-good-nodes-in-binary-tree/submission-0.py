# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,maxi):
            if node == None:
                return 0
            count=0
            if node.val>=maxi:
                count=1
            maxi=max(maxi,node.val)
            left=dfs(node.left,maxi)
            right=dfs(node.right,maxi)
            return count+left+right
        return dfs(root,root.val)