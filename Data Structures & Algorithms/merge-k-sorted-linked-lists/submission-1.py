# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return None
        def mergelists(l1,l2):
            dummy=ListNode(0)
            end=dummy
            if not l1 and not l2:
                return []
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
        for i in range(1,len(lists)):
            lists[i]=mergelists(lists[i-1],lists[i])
        return lists[-1]
