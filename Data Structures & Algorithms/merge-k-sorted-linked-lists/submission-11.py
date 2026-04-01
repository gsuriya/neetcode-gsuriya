# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """

        merge sort
        perform merge function on logn levels

           
           L        R
        [1,2,4], [1,3,5], [3,6], [4, 6]

        """
        if not lists:
            return None

        def merge_sort(L, R):
            if L >= R:
                return lists[L]
            
            mid = (L+R) // 2
            
            # merged lists from L and R
            left = merge_sort(L, mid)
            right = merge_sort(mid+1, R)
            
            return self.merge(left, right)
        
        return merge_sort(0, len(lists)-1)


    def merge(self, l1, l2):
        c1, c2 = l1, l2
        c3 = dummy = ListNode(-1)

        while c1 and c2:
            if c1.val <= c2.val:
                c3.next = c1
                c1 = c1.next
            else:
                c3.next = c2
                c2 = c2.next
            c3 = c3.next
        
        if c1:
            c3.next = c1
        if c2:
            c3.next = c2

        return dummy.next












