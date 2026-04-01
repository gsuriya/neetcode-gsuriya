class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Cycle linked list problem, each int index
        # represents the .next pointer 

        """ 
        Regular Floyd's algo

        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        
        slow2 = head
        while slow2 != slow:
            slow2 = slow2.next
            slow = slow.next
        
        return slow
        """

        fast, slow = 0, 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow: # if the INDICES (pointers) equal, NOT THE .VAL's
                break
        
        slow2 = 0
        while slow2 != slow:
            slow2 = nums[slow2]
            slow = nums[slow]

        return slow2    

