# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        leftptr = dummy
        rightptr = head

        for _ in range(left - 1):
            leftptr = rightptr
            rightptr = rightptr.next
        
       
        prev = None
        for _ in range(right - left + 1):
            temp = rightptr.next
            rightptr.next = prev
            prev = rightptr
            rightptr = temp
            
        leftptr.next.next = rightptr
        leftptr.next = prev
        return dummy.next