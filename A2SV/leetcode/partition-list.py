# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left = ListNode()
        right = ListNode()

        leftptr = left
        rightptr = right

        while head:
            if head.val < x:
                leftptr.next = head #1 is head, 2 is head
                leftptr = leftptr.next # 1-> 2, 
            else:
                rightptr.next = head #4 is head, 3 is head, 
                rightptr = rightptr.next #4->3, 3 ->5
            head = head.next #since 2-> 2, then breaks it now points to none
        rightptr.next = None
        leftptr.next = right.next #end of the leftptr will point to the head of right.next cause the right is only ) we want it to point to the number next to right which is 4 
        #to connect the two then return left.next to shift the dummy node by 1 cause again the value starts at 0 but we want it to start from where the vlaue we added begun
        return left.next
        