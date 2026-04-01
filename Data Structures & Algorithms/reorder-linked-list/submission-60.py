# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """

        1. break list in half (left half should have more if odd)
        - F one ahead of slow (works for both even and odd sized lists)
        2. reverse second list
        3. process them in correct order and string together


        """

        # step 1: break into 2 lists
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        c1, c2 = head, slow.next
        slow.next = None

        # step 2: reverse second list
        prev = None
        tmp = c2
        while c2:
            tmp = c2.next
            c2.next = prev
            prev = c2
            c2 = tmp
        c2 = prev

        # step 3: process in correct order and string together
        """

                 c1   c2
        2 -> 4 -> 6 t   8 <- 10

        2 -> 10 -> 4 -> 8 -> 6 -> none

        """
        while c2:
            tmp = c1.next
            c1.next = c2
            c1 = tmp

            tmp = c2.next
            c2.next = c1
            c2 = tmp





        

