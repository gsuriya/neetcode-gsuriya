# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """

        remove the 1 (n = 4)

          L           R
        dummy -> 1 -> 2 -> 3 -> 4 -> None

        1. initialize L and R at dummy
        2. move R n+1 spaces foward
        3. move L and R together until R reaches the end
        - remove node in front of L

        """
        # initialize
        L = R = dummy = ListNode(-1, head)

        # move R forward initially
        count = n+1
        while count:
            R = R.next
            count -= 1

        # move L and R together
        while R:
            L = L.next
            R = R.next
        
        # remove node in front of L
        L.next = L.next.next
        
        return dummy.next
        
        

