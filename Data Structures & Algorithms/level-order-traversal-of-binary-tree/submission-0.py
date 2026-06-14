# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        r=[]
        st=[root]
        while len(st)!=0:
            x=len(st)
            l=[]
            for i in range(x):
                q=st.pop(0)
                l.append(q.val)
                if q.left!=None:
                    st.append(q.left)
                if q.right!=None:
                    st.append(q.right)
            r.append(l)
        return r