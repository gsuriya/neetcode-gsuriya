class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # O(1) space, so LL cycle head on array

        # the dup is the index w/ two same .next
        # each index in arr is a .next pointer

        fast, slow = 0, 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]

            if fast == slow:
                break
        
        slow2 = 0
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]

            if slow2 == slow:
                return slow2