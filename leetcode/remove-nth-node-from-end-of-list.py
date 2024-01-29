# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy # 0
        right = head

        while n > 0 and right: # to make the risht first point at 3 by shifting it using a loop
            right = right.next
            n -= 1
        while right: # keep shifting till the end of the loop 
            left = left.next
            right = right.next
        left.next = left.next.next # take 3 and let it point to 5
        return dummy.next # not starting from 0 but starting from 1