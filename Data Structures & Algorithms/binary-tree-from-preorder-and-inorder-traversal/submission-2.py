# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mp={}
        for i in range(len(inorder)):
            mp[inorder[i]]=i
        self.pre=0
        def dfs(left,right):
            if left>right:
                return None
            root=TreeNode(preorder[self.pre])
            self.pre+=1
            mid=mp[root.val]
            root.left=dfs(left,mid-1)
            root.right=dfs(mid+1,right)
            return root
        return dfs(0,len(inorder)-1)
