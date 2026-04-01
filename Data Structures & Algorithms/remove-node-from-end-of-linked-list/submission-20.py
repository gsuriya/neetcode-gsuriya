# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """

        n = 2 (remove node.val = 3)
        
        therefore, space btwn A and B @ start = n+1
        move B by n

             A               B                                
        1 -> 2 -> 4 -> null

   A          B
        1 -> null

        while A and B
            A = A.next
            B = B.next

        All cases
        - remove node from middle (and end)
        - remove node from beginning

        edge: 1 node list

        - remove from beginning:
            if B is null at the very start, meaning n = len(LL), move head
            1 node list edge also fits into here

        """
        A = dummy = ListNode(-1)
        A.next = head
        B = head

        # move b by n
        while n > 0:
            B = B.next
            n -= 1
        
        

        # move both A and B together
        while B:
            B = B.next
            A = A.next
        
        # delete node after A
        A.next = A.next.next
        return dummy.next

        