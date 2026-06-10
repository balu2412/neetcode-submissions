# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l=0
        curr=head
        while curr!=None:
            curr=curr.next
            l+=1
        if n==1 and l==1:
            return None
        if n==l:
            return head.next
        a=l-n-1
        curr=head
        for i in range(a):
            curr=curr.next
        curr.next=curr.next.next
        return head