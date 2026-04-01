# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
       111
        389
       9654
      10043


             c1
        9 --> 8 -> 3

        +

             c2
        4 --> 5 --> 6 --> 9

        =
        
        3 --> 

        """

        c1, c2 = l1, l2
        carry = 0
        c3 = dummy = ListNode(-1)

        while c1 or c2 or carry:
            # find sum and carry
            v1 = c1.val if c1 else 0
            v2 = c2.val if c2 else 0

            total = v1 + v2 + carry # 13
            carry = 1 if total >= 10 else 0 # 1
            sum_ = total % 10 # 3

            # append next node
            c3.next = ListNode(sum_)
            c3 = c3.next

            # move pointers
            if c1:
                c1 = c1.next
            if c2:
                c2 = c2.next

        return dummy.next







