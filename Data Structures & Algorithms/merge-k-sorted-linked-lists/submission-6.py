# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""

                     L       R                       
[ [1,2,4], [1,3,5], [3,6], [4,5] ]

"""

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        return self.merge_sort(lists, 0, len(lists)-1)

    def merge_sort(self, LL_arr, L, R):
        if L >= R:
            return LL_arr[L]
        
        mid = (L+R) // 2
        left = self.merge_sort(LL_arr, L, mid)
        right = self.merge_sort(LL_arr, mid+1, R)
        return self.merge(left, right)

    # merge two sorted linked lists
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

        if not c1:
            c3.next = c2
        elif not c2:
            c3.next = c1

        return dummy.next







