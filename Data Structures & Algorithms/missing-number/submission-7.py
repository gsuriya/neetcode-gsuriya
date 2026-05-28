class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """

        find missing number using bitwise operations

        generate counterpart range for XOR

        1. xor all in [0, n] together
        2. xor all in nums arr
        3. xor both --> gives missing number


        0 1 2
        0   2

        0 ^ 1 ^ 2 ^ 0 ^ 2
        0 ^ 0 ^ 2 ^ 2 ^ 1 --> 1

        """
        res = 0

        # xor all in [0, n] range
        for i in range(len(nums)+1):
            res ^= i
        # xor all in nums
        for n in nums:
            res ^= n

        return res


        