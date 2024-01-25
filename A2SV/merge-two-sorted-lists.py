# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        one = list1
        two = list2
        dummy = ListNode()
        placer = dummy
        while one != None or two != None:
            if one and (not two or one.val <= two.val):
                placer.next = one
                one = one.next
            else:
                placer.next = two
                two = two.next
            placer = placer.next
        # if it was invalid the placer.next = one - if one was valid 
        # or we can make it placer.next = two - if two was valid

        return dummy.next
        