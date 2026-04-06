# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """

        go thru list in order of processing

        1. find middle of list (1st is longer)
        2. reverse second list
        3. merge both at same time

          3
        dummy -> 2 --> 10 --> 4 --> 8 --> 6

                  1  2
        2 -> 4 -> 6   8 <- 10

        """

        # find middle
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        c2 = slow.next
        slow.next = None
        c1 = head
    
        # reverse second list
        tmp = c2
        prev = None
        while c2:
            tmp = c2.next
            c2.next = prev
            prev = c2
            c2 = tmp
        c2 = prev

        # merge both lists
        c3 = dummy = ListNode(-1)
        alternator = 1
        while c1 or c2:
            if alternator == 1:
                c3.next = c1
                c1 = c1.next
                alternator = 2
            elif alternator == 2:
                c3.next = c2
                c2 = c2.next
                alternator = 1
            c3 = c3.next
        
        head = dummy.next
        


            

        

        

