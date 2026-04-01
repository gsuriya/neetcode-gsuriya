# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # neetcode did this wrong, he used O(n) space
        # do O(1) solution myself later
        dummy = curr3 = ListNode(-1)
        
        curr1 = l1
        curr2 = l2

        # l1 = [9]
        # l2 = [9]

        # dum --> 8

        # total = 18
        # sum = 8
        # carry = 1

        carry = 0
        while curr1 or curr2 or carry: # if carry == 1 @ the end, curr3.next = ListNode(carry)
            if not curr1:
                part1 = 0
            else:
                part1 = curr1.val
            if not curr2:
                part2 = 0
            else: 
                part2 = curr2.val
            
            total = part1 + part2 + carry
            carry = 1 if total >= 10 else 0
            sum_ = total % 10

            curr3.next = ListNode(sum_)
            curr3 = curr3.next

            if curr1:
                curr1 = curr1.next
            if curr2:
                curr2 = curr2.next

        return dummy.next
            