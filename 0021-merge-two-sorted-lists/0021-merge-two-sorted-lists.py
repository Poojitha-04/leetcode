# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res=ListNode()
        curr=res
        if not list1 and not list2: return None
        if not list1: return list2
        if not list2: return list1
        while list1 is not None and list2 is not None:
            if list1.val<=list2.val:
                curr.next=list1
                list1=list1.next
            else:
                curr.next=list2
                list2=list2.next
            curr=curr.next
        if not list1:
            curr.next=list2
        if not list2:
            curr.next=list1
        return res.next
    



