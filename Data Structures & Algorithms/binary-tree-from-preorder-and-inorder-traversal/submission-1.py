# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pi=ii=0
        def dfs(limit):
            nonlocal pi,ii
            if pi>=len(preorder):
                return None
            if inorder[ii]==limit:
                ii+=1
                return None
            root=TreeNode(preorder[pi])
            pi+=1
            root.left=dfs(root.val)
            root.right=dfs(limit)
            return root
        return dfs(float('inf'))