# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        trav = head
        prev = None
        while trav:
            temp = trav.next
            trav.next = prev
            prev = trav
            trav = temp
        return prev