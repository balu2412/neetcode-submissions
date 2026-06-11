# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return 
        st=[]
        curr=head
        while curr!=None:
            st.append(curr)
            curr=curr.next
        n=len(st)
        curr=head
        for i in range(n//2):
            last=st.pop()
            nxt=curr.next
            curr.next=last
            last.next = nxt
            curr = nxt
        curr.next = None
