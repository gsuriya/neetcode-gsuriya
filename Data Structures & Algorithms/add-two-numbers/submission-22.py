# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
                                c1
        1 --> 2 --> 3 --> 9 -> null

                          c2
        9 --> 5 --> 6 -> null

              c1
        9 -> null

              c2
        9 -> null

    c3
    -1 -> 0 -> 8 -> 9    

       - calculated sum and carry
       - add new nodes to new list
          1
        4321
         659
        ----
        4980
        """
        c1, c2 = l1, l2
        c3 = dummy = ListNode(-1)

        carry = 0
        while c1 or c2 or carry:
            # calculate sum and carry
            c1_val, c2_val = c1.val if c1 else 0, c2.val if c2 else 0 
            total = c1_val + c2_val + carry
            sum_ = total % 10
            carry = 1 if total >= 10 else 0

            # add new nodes to new list
            c3.next = ListNode(sum_)

            # move pointers
            if c1:
                c1 = c1.next
            if c2:
                c2 = c2.next
            c3 = c3.next
        
        return dummy.next


