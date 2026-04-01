# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
       
        1
        3 2 1
    +   7 8 4
    ---------
      1 1 0 5

        1 --> 2 --> 3

        4 --> 8 --> 7

        """

        c1, c2 = l1, l2
        c3 = dummy = ListNode(-1)
        carry = 0

        while c1 or c2 or carry:
            first = c1.val if c1 else 0
            second = c2.val if c2 else 0

            total = first + second + carry
            sum_ = total % 10
            carry = total // 10

            c3.next = ListNode(sum_)
            c3 = c3.next

            if c1:
                c1 = c1.next
            if c2:
                c2 = c2.next
        
        return dummy.next


        