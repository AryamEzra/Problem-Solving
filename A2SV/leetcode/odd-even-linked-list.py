# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #we are not checking for the values inside of them reather the positions at which they are odd or even
        if head == None:
            return 
        odd = head
        even = odd.next

        start_even = even
        while even is not None and even.next is not None:
            odd.next = even.next #1->3
            odd = odd.next # the value we had just arrived the 3 is not the odd
            even.next = odd.next #2->4 beacuse we were at 3 and the value next to 3 is 4 thereforew e should set 2 to 4
            even = even.next # our prevoius value was 2 and now we set that to equal to 4 then since the loop will end having the evn point to none then finally make the odd's tail become the even's
        odd.next = start_even
        return head
        
        


        


        