class Solution:
    """
    CHECK IF SLOW2 AND SLOW MEET RIGHT AWAY, DON'T MOVE FIRST
    """
    def findDuplicate(self, nums: List[int]) -> int:
        # O(1) space, so LL cycle head on array

        # the dup is the index w/ two same .next
        # each index in arr is a .next pointer

        fast, slow = nums[0], nums[0]
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]

            if fast == slow:
                break
        
        slow2 = nums[0]
        while slow2 != slow:
            slow2 = nums[slow2]
            slow = nums[slow]
            
        return slow2

            

            