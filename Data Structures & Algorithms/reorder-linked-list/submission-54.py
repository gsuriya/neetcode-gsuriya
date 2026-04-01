# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        
            c1          t c2
        0 -> 1             2

        0 -> 2


        1. find midpoint - first list should have more
        2. break apart, reverse 2nd list
        3. iterate through both lists, combining


        """

        # find midpoint
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # break apart, reverse 2nd list
        c1, c2 = head, slow.next
        slow.next = None
        tmp = c2
        prev = None

        while c2:
            tmp = c2.next
            c2.next = prev
            prev = c2
            c2 = tmp
        c2 = prev

        # iterate through both lists, combining
        while c1 and c2:
            tmp = c1.next
            c1.next = c2
            c1 = tmp

            tmp = c2.next
            c2.next = c1
            c2 = tmp
        
        return None


        




