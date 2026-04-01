# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def rev(start):
            if not start:
                return None
            
            # move end k-1 away 
            # - DO NOT REVERSE if less than k nodes
            reverse = True
            end = curr = tmp = start
            count = k-1
            while count and end.next:
                end = end.next
                count -= 1 
            if count: reverse = False
            next_start = end.next

            # reverse from [start, end] 
            if reverse:
                prev = None
                while curr != next_start:
                    tmp = curr.next
                    curr.next = prev
                    prev = curr
                    curr = tmp
            else:
                return start
            
            start.next = rev(next_start)
            return end


        return rev(head)





