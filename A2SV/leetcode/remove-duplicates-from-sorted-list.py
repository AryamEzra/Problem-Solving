# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = cur
        while cur is not None: #hasn't reached the end of the linked list
            if cur.val == prev.val:
                cur = cur.next
                prev.next = cur
            else:
                prev = cur
                cur = cur.next
        return head





        