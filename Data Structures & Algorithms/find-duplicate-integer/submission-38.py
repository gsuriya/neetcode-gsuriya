class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """

        tortoise and hare problem w array

        F    
        1 2 3 2 2
        0 1 2 3 4


        """
        fast, slow = nums[0], nums[0]

        # fast and slow pointers until intersect
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]

            if fast == slow:
                break
        
        # start slow2 pointer
        slow2 = nums[0]
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        
        return slow

