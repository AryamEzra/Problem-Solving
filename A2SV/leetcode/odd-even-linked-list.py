# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #we are not checking for the values inside of them reather the positions at which they are odd or even
        #if it has no elem, then only 1 odd elem, then 2 ele odd and even then just return them as is
        if not head or not head.next or not head.next.next:
            return head

        odd = head
        cur = head
        even = head.next
        start_even = head.next
        
        i = 1

        while cur:
            #here i > 2 becuase we already reserved odd and first as the first two  
            if i > 2 and i % 2 == 1:
                odd.next = cur
                odd = odd.next
            elif i > 2 and i % 2 == 0:
                even.next = cur
                even = even.next
            cur = cur.next 
            i += 1
        even.next = None #the even should be none
        odd.next = start_even # the odd should point twoards the head of the even in the end
        return head


        


        