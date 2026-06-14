# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr=[]
        for i in lists:
            while i:
                arr.append(i.val)
                i=i.next
        arr.sort()
        dummy=ListNode(0)
        curr=dummy
        for i in arr:
            curr.next=ListNode(i)
            curr=curr.next
        return dummy.next