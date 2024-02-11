# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        prev = dummy 

        while head:  
            after = head.next 
            if prev.val >= head.val: 
                prev = dummy
            while prev.next and prev.next.val < head.val: 
                prev = prev.next
            head.next = prev.next 
            prev.next = head 
            head = after 
        return dummy.next