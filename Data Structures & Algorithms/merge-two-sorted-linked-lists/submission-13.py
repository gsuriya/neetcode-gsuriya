# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr3 = ListNode()
        # dummy to return head at the end
        # curr3 for final list iteration pointer

        curr1 = list1
        curr2 = list2

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                curr3.next = curr1
                curr1 = curr1.next
            else: # curr1.val > curr2.val
                curr3.next = curr2
                curr2 = curr2.next
            curr3 = curr3.next
        
        # remainders
        if curr1:
            curr3.next = curr1
        elif curr2:
            curr3.next = curr2
        
        return dummy.next
