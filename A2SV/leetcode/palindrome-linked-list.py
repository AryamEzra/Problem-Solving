# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return

        fast = head
        slow = head
        start = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #reverse the second half
        first = slow
        prev = None

        while first:
            tmp = first.next
            first.next = prev
            prev = first
            first = tmp

        while start and start != slow:
            if start.val == prev.val:
                start = start.next
                prev = prev.next
            else:
                return False
        return True

        

        

        

