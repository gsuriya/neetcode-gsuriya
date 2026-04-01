# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """

        n = 2
        
        R = n+1

                   L              R
        -1 -> 1 -> 2 -> 3 -> 4

                  R
        L
        -1 -> 5

        """

        L = R = dummy = ListNode(-1, head)

        count = n+1
        while count:
            R = R.next
            count -= 1

        while R:
            R = R.next
            L = L.next
        
        L.next = L.next.next

        return dummy.next