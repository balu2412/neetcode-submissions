# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return None
        if l1 is None and l2!=None:
            return l2 
        if l2 is None and l1!=None:
            return l1
        dummy=ListNode(0)
        end=dummy 
        while l1 and l2:
            if l1.val<l2.val:
                end.next=l1
                l1=l1.next
            else:
                end.next=l2
                l2=l2.next
            end=end.next
        end.next=l1 or l2
        return dummy.next







