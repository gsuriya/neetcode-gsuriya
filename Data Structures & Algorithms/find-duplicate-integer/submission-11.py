class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
         0 1 2 3 4
        [1,2,3,4,4]

        1 --> 2 --> 3 --> 4 --> 4
                          ^    |
                          |-----

        each int represents the .next pointer (index val)
        
        since there are 2 nodes that point to 4, this means that 4 is the start of the cycle
        --> therefore, 4 is the duplicate

        1. create LL diagram
        2. implemenet fast and slow pointer algo

        """
        """
        General Floyd algo to return start of cycle
        while curr:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break

        slow2 = head
        while slow != slow2:
            slow = slow.next
            slow2 = slow2.next
        return slow2 # returns node that is start of cycle
        """
        fast, slow = 0, 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break
        
        slow2 = 0
        while slow2 != slow:
            slow2 = nums[slow2]
            slow = nums[slow]
        
        return slow2
        

