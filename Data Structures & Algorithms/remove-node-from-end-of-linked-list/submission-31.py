# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        n = 2
        val to remove: 1

        L/R spacing: n+1

                 L                R
    dummy -> 1 -> 2 -> 3 -> 4

        1. initialize L and R, move R n+1 times
        2. move both L and R until R null
        3. remove node in front of L

        """
        # step 1
        dummy = L = R = ListNode(-1, head)
        for i in range(n+1):
            R = R.next
        
        # step 2
        while R:
            R = R.next
            L = L.next
        
        # step 3
        L.next = L.next.next
    
        return dummy.next


