class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """

        generate counterpart range from 0-n and XOR both counterpart range and nums in list
        - number remaining is the missing one


        [0, 2]

        0   2
        0 1 2

        0 ^ 2 ^ 0 ^ 1 ^ 2
        0 ^ 0 ^ 2 ^ 2 ^ 1 --> 1

        """

        res = 0
        
        # numbers in list
        for n in nums: res ^= n

        # counterpart range
        for i in range(0, len(nums)+1): res ^= i
        
        return res