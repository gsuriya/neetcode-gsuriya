class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # O(1) space so think TWO POINTERS
        slow, fast = 0, 0

        # cycle detection
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        # head of cycle
        slow2 = 0
        while True: # head of cycle CANT be at index 0 b/c no range is [1,n]
            slow = nums[slow]
            slow2 = nums[slow2]
            
            if slow == slow2:
                return slow