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

        # xor all nums in list
        res = 0
        for n in nums: res ^= n

        # xor all nums in counterpart range
        for i in range(0, len(nums)+1): res ^= i

        # xor together
        return res