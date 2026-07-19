# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res=[]
        stack=[root]
        while (len(stack))!=0:
            x=len(stack)
            list_=[]
            for i in range(x):
                q=stack.pop(0)
                list_.append(q.val)
                if q.left!=None:
                    stack.append(q.left)
                if q.right!=None:
                    stack.append(q.right)
            res.append(list_)
        return res



